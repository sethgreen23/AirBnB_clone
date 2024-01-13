#!/usr/bin/python3
"""Unittest for class Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class TestReviewClass(unittest.TestCase):
    """Unittest class for testing class Review
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
"""
    def setUp(self):
        """setUp method"""
        self.r1 = Review()
        self.r2 = Review()
        # dict_storage = storage.all()
        # dict_storage = {}

    def tearDown(self):
        """tearDown method"""
        del self.r1
        del self.r2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_Review_id(self):
        """Test Review instance id"""
        self.assertNotEqual(self.r1.id, self.r2.id)

    # ***************************************************************
    def test_Review_name(self):
        """Test Review place id"""
        self.assertIsInstance(self.r1.place_id, str)
        self.r1.place_id = "ET.AA"
        self.assertEqual(self.r1.place_id, "ET.AA")

        self.assertIsInstance(self.r1.text, str)
        self.r1.text = "The place is very good."
        self.assertEqual(self.r1.text, "The place is very good.")

    def test_Review_user_id(self):
        """Test Review user id"""
        self.assertIsInstance(self.r1.user_id, str)
        self.r1.user_id = "rocky9"
        self.assertEqual(self.r1.user_id, "rocky9")

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.r1.created_at, datetime)
        self.assertIsInstance(self.r1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for Review class attributes"""
        self.assertEqual(self.r1.place_id, "")
        self.assertEqual(self.r1.user_id, "")
        self.assertEqual(self.r1.text, "")

    def test_Review_inherits_BaseModel(self):
        """Test if Review inherits from BaseModel"""
        self.assertIsInstance(self.r1, BaseModel)

    def test_Review_type(self):
        """Test if Review instance is of the same type"""
        self.assertEqual(type(self.r1), Review)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.r1.__class__.__name__}.{self.r1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.r2.__class__.__name__}.{self.r2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.r1.save()
        self.r2.save()

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_r1 = self.r1.to_dict()
        self.assertIsInstance(dict_r1, dict)
        self.assertIn('id', dict_r1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_r1 = self.r1.to_dict()
        self.assertIsInstance(dict_r1, dict)
        self.assertIn('created_at', dict_r1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_r1 = self.r1.to_dict()
        self.assertIsInstance(dict_r1, dict)
        self.assertIn('updated_at', dict_r1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_r1 = self.r1.to_dict()
        self.assertEqual(self.r1.__class__.__name__, dict_r1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.r1)
        format = "[{}] ({}) {}".format(self.r1.__class__.__name__,
                                       self.r1.id, self.r1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_r1 = self.r1.to_dict()
        instance = Review(**dict_r1)
        self.assertIsNot(self.r1, instance)
        self.assertEqual(str(self.r1), str(instance))
        self.assertFalse(instance is self.r1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.r1.updated_at
        time.sleep(0.1)
        self.r1.save()
        updated_new = self.r1.updated_at
        self.assertNotEqual(update_old, updated_new)
