#!/usr/bin/python3
""" Test of File Storage """
from models.engine.file_storage import FileStorage
import models
import unittest
import os


class Test_FileStorage(unittest.TestCase):
    """ Test of FIle Storage """

    def setUp(self):
        """SetUp method"""
        self.file_storage = FileStorage()

    def TearDown(self):
        """TearDown method."""
        del self.file_storage

    def test_type(self):
        """Test type of class"""
        self.assertIsInstance(self.file_storage, FileStorage)
        self.assertEqual(
            str(type(self.file_storage)), "<class 'models.engine.file_storage.FileStorage'>")

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
        """Test docs for class"""
        self.assertIsNotNone(
            models.engine.file_storage.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(FileStorage.__doc__, "No docstring in the class")
