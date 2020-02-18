#!/usr/bin/python3
""" Test of BaseModel """
from models.base_model import BaseModel
import unittest
import datetime


class Test_Base(unittest.TestCase):
    """ Test of BaseModel """

    def test_creation(self):
        """ Test creation of an object """
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)

    def test_obj_to_dict(self):
        """ Test if is an instance """
        a = BaseModel()
        self.assertIsInstance(a.to_dict(), dict)

    def test_str_rep(self):
        """ Test string representation """
        a = BaseModel()
        self.assertIsInstance(a.__str__(), str)

    def test_id(self):
        """ Test if each ID is different """
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_date_time(self):
        """ Test if update and create are datetime """
        a = BaseModel()
        self.assertIsInstance(type(a.created_at), type(datetime.datetime))
        self.assertIsInstance(type(a.updated_at), type(datetime.datetime))

    def test_save(self):
        """ Test if updated_at is working correctly"""
        a = BaseModel()
        first = a.updated_at
        a.save()
        self.assertNotEqual(first, a.updated_at)
