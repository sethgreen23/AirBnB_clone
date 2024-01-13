#!/usr/bin/python3
"""Unittest for class City"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class TestCityClass(unittest.TestCase):
    """Unittest class for testing class City
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
"""
    def setUp(self):
        """setUp method"""
        self.c1 = City()
        self.c2 = City()
        # dict_storage = storage.all()
        # dict_storage = {}

    def tearDown(self):
        """tearDown method"""
        del self.c1
        del self.c2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_City_id(self):
        """Test City instance id"""
        self.assertNotEqual(self.c1.id, self.c2.id)

    # ***************************************************************
    def test_City_name(self):
        """Test City name"""
        self.assertIsInstance(self.c1.name, str)
        self.c1.name = "Addis Ababa"
        self.assertEqual(self.c1.name, "Addis Ababa")

    def test_City_state_id(self):
        """Test City state id"""
        self.assertIsInstance(self.c1.state_id, str)
        self.c1.state_id = "ET.AA"
        self.assertEqual(self.c1.state_id, "ET.AA")

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for City class attributes"""
        self.assertEqual(self.c1.name, "")

    def test_City_inherits_BaseModel(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.c1, BaseModel)

    def test_City_type(self):
        """Test if City instance is of the same type"""
        self.assertEqual(type(self.c1), City)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.c1.__class__.__name__}.{self.c1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.c2.__class__.__name__}.{self.c2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.c1.save()
        self.c2.save()

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('id', dict_c1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('created_at', dict_c1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('updated_at', dict_c1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertEqual(self.c1.__class__.__name__, dict_c1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.c1)
        format = "[{}] ({}) {}".format(self.c1.__class__.__name__,
                                       self.c1.id, self.c1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_c1 = self.c1.to_dict()
        instance = City(**dict_c1)
        self.assertIsNot(self.c1, instance)
        self.assertEqual(str(self.c1), str(instance))
        self.assertFalse(instance is self.c1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.c1.updated_at
        time.sleep(0.1)
        self.c1.save()
        updated_new = self.c1.updated_at
        self.assertNotEqual(update_old, updated_new)
