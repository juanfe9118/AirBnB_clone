#!/usr/bin/python3
""" Test of File Storage """
from models.engine.file_storage import FileStorage
import models
import unittest
import datetime
import os


class Test_File_Storage(unittest.TestCase):
    """ Test of FIle Storage """

    def test_creation(self):
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

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

    def test_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.__doc__)
