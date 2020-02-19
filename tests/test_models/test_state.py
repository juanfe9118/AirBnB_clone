#!/usr/bin/python3
"""Test module of State"""
from models.state import State
import unittest
import datetime
import os


class Test_State(unittest.TestCase):
    """Test class of State"""

    def test_creation(self):
        """ Test creation of an object """
        a = State()
        self.assertIsInstance(a, State)

    def test_obj_to_dict(self):
        """ Test if is an instance and how it print """
        a = State()
        self.assertIsInstance(a.to_dict(), dict)
        for k, v in a.to_dict().items():
            f = 0
            if k == '__class__':
                f = 1
            if k == 'created_at':
                self.assertIsInstance(v, str)
            if k == 'updated_at':
                self.assertIsInstance(v, str)
        self.assertEqual(f, 1)

    def test_str_rep(self):
        """ Test string representation """
        a = State()
        self.assertIsInstance(a.__str__(), str)
        dic = a.__dict__
        s1 = a.__str__()
        s2 = '[State] ({}) {}'.format(a.id, dic)
        self.assertEqual(s1, s2)

    def test_id(self):
        """ Test if each ID is different """
        a = State()
        b = State()
        self.assertNotEqual(a.id, b.id)

    def test_date_time(self):
        """ Test if update and create are datetime """
        a = State()
        self.assertIsInstance(type(a.created_at), type(datetime.datetime))
        self.assertIsInstance(type(a.updated_at), type(datetime.datetime))

    def test_save(self):
        """ Test if updated_at is working correctly"""
        a = State()
        first = a.updated_at
        a.save()
        self.assertNotEqual(first, a.updated_at)

    def test_permissions(self):
        """ Test Permissions """
        # Read permissions
        r = os.access('models/state.py', os.R_OK)
        self.assertTrue(r)
        # Write permissions
        w = os.access('models/state.py', os.W_OK)
        self.assertTrue(r)
        # Execute permissions
        e = os.access('models/state.py', os.X_OK)
        self.assertTrue(r)

    def test_create_kw(self):
        dic = {"id": "cec8988f-182e-45ce-934b-1e85aedf55c3",
               "created_at": "2020-02-18T13:34:09.711961",
               "updated_at": "2020-02-18T13:34:09.711965"}
        a = State(**dic)
        cr = datetime.datetime(2020, 2, 18, 13, 34, 9, 711961)
        up = datetime.datetime(2020, 2, 18, 13, 34, 9, 711965)
        self.assertEqual(a.id, "cec8988f-182e-45ce-934b-1e85aedf55c3")
        self.assertEqual(cr, a.created_at)
        self.assertEqual(up, a.updated_at)
        self.assertEqual(a.__class__.__name__, "State")

    def test_doc(self):
        self.assertIsNotNone(State.__doc__)
        a = State()
        self.assertIsNotNone(a.__str__.__doc__)
        self.assertIsNotNone(a.save.__doc__)
        self.assertIsNotNone(a.to_dict.__doc__)
