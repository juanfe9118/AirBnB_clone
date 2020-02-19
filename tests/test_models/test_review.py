#!/usr/bin/python3
""" Test of Review """
from models.review import Review
import unittest
import datetime
import os


class Test_Review(unittest.TestCase):
    """ Test of Review """

    def test_creation(self):
        """ Test creation of an object """
        a = Review()
        self.assertIsInstance(a, Review)

    def test_obj_to_dict(self):
        """ Test if is an instance and how it print """
        a = Review()
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
        a = Review()
        self.assertIsInstance(a.__str__(), str)
        dic = a.__dict__
        s1 = a.__str__()
        s2 = '[Review] ({}) {}'.format(a.id, dic)
        self.assertEqual(s1, s2)

    def test_id(self):
        """ Test if each ID is different """
        a = Review()
        b = Review()
        self.assertNotEqual(a.id, b.id)

    def test_date_time(self):
        """ Test if update and create are datetime """
        a = Review()
        self.assertIsInstance(type(a.created_at), type(datetime.datetime))
        self.assertIsInstance(type(a.updated_at), type(datetime.datetime))

    def test_save(self):
        """ Test if updated_at is working correctly"""
        a = Review()
        first = a.updated_at
        a.save()
        self.assertNotEqual(first, a.updated_at)

    def test_permissions(self):
        """ Test Permissions """
        # Read permissions
        r = os.access('models/review.py', os.R_OK)
        self.assertTrue(r)
        # Write permissions
        w = os.access('models/review.py', os.W_OK)
        self.assertTrue(r)
        # Execute permissions
        e = os.access('models/review.py', os.X_OK)
        self.assertTrue(r)

    def test_create_kw(self):
        dic = {"id": "cec8988f-182e-45ce-934b-1e85aedf55c3",
               "created_at": "2020-02-18T13:34:09.711961",
               "updated_at": "2020-02-18T13:34:09.711965"}
        a = Review(**dic)
        cr = datetime.datetime(2020, 2, 18, 13, 34, 9, 711961)
        up = datetime.datetime(2020, 2, 18, 13, 34, 9, 711965)
        self.assertEqual(a.id, "cec8988f-182e-45ce-934b-1e85aedf55c3")
        self.assertEqual(cr, a.created_at)
        self.assertEqual(up, a.updated_at)
        self.assertEqual(a.__class__.__name__, "Review")

    def test_doc(self):
        self.assertIsNotNone(Review.__doc__)
        a = Review()
        self.assertIsNotNone(a.__str__.__doc__)
        self.assertIsNotNone(a.save.__doc__)
        self.assertIsNotNone(a.to_dict.__doc__)
