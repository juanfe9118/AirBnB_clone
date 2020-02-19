#!/usr/bin/python3
""" Test of File Storage """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
import os


class Test_File_Storage(unittest.TestCase):
    """ Test of FIle Storage """

    def test_creation(self):
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

    def test_objects(self):
        a = FileStorage()
        self.assertIsInstance(a.all(), dict)
        b = BaseModel()
        id = b.id
        s1 = b.__class__.__name__+"."+b.id
        s2 = a.all().keys()
        self.assertIn(s1, s2)

    def test_permissions(self):
        """ Test Permissions """
        # Read permissions
        r = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(r)
        # Write permissions
        w = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(r)
        # Execute permissions
        e = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(r)
