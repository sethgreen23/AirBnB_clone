#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class TestAmenityClass(unittest.TestCase):
    """Unittest class for testing class Amenity
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
"""
    def setUp(self):
        """setUp method"""
        self.a1 = Amenity()
        self.a2 = Amenity()
        # dict_storage = storage.all()
        # dict_storage = {}

    def tearDown(self):
        """tearDown method"""
        del self.a1
        del self.a2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_Amenity_id(self):
        """Test Amenity instance id"""
        self.assertNotEqual(self.a1.id, self.a2.id)

    # ***************************************************************
    def test_Amenity_name(self):
        """Test Amenity name"""
        self.assertIsInstance(self.a1.name, str)
        self.a1.name = "Fridge"
        self.assertEqual(self.a1.name, "Fridge")

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.a1.created_at, datetime)
        self.assertIsInstance(self.a1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for Amenity class attributes"""
        self.assertEqual(self.a1.name, "")

    def test_Amenity_inherits_BaseModel(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertIsInstance(self.a1, BaseModel)

    def test_Amenity_type(self):
        """Test if Amenity instance is of the same type"""
        self.assertEqual(type(self.a1), Amenity)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.a1.__class__.__name__}.{self.a1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.a2.__class__.__name__}.{self.a2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.a1.save()
        self.a2.save()

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_a1 = self.a1.to_dict()
        self.assertIsInstance(dict_a1, dict)
        self.assertIn('id', dict_a1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_a1 = self.a1.to_dict()
        self.assertIsInstance(dict_a1, dict)
        self.assertIn('created_at', dict_a1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_a1 = self.a1.to_dict()
        self.assertIsInstance(dict_a1, dict)
        self.assertIn('updated_at', dict_a1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_a1 = self.a1.to_dict()
        self.assertEqual(self.a1.__class__.__name__, dict_a1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.a1)
        format = "[{}] ({}) {}".format(self.a1.__class__.__name__,
                                       self.a1.id, self.a1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_a1 = self.a1.to_dict()
        instance = Amenity(**dict_a1)
        self.assertIsNot(self.a1, instance)
        self.assertEqual(str(self.a1), str(instance))
        self.assertFalse(instance is self.a1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.a1.updated_at
        time.sleep(0.1)
        self.a1.save()
        updated_new = self.a1.updated_at
        self.assertNotEqual(update_old, updated_new)
