#!/usr/bin/python3
"""Unittest for class State"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class TestStateClass(unittest.TestCase):
    """Unittest class for testing class State
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
"""
    def setUp(self):
        """setUp method"""
        self.s1 = State()
        self.s2 = State()
        # dict_storage = storage.all()
        # dict_storage = {}

    def tearDown(self):
        """tearDown method"""
        del self.s1
        del self.s2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_State_id(self):
        """Test State instance id"""
        self.assertNotEqual(self.s1.id, self.s2.id)

    # ***************************************************************
    def test_State_name(self):
        """Test State name"""
        self.assertIsInstance(self.s1.name, str)
        self.s1.name = "Tunis"
        self.assertEqual(self.s1.name, "Tunis")

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.s1.created_at, datetime)
        self.assertIsInstance(self.s1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for State class attributes"""
        self.assertEqual(self.s1.name, "")

    def test_State_inherits_BaseModel(self):
        """Test if State inherits from BaseModel"""
        self.assertIsInstance(self.s1, BaseModel)

    def test_State_type(self):
        """Test if State instance is of the same type"""
        self.assertEqual(type(self.s1), State)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.s1.__class__.__name__}.{self.s1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.s2.__class__.__name__}.{self.s2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.s1.save()
        self.s2.save()

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_s1 = self.s1.to_dict()
        self.assertIsInstance(dict_s1, dict)
        self.assertIn('id', dict_s1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_s1 = self.s1.to_dict()
        self.assertIsInstance(dict_s1, dict)
        self.assertIn('created_at', dict_s1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_s1 = self.s1.to_dict()
        self.assertIsInstance(dict_s1, dict)
        self.assertIn('updated_at', dict_s1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_s1 = self.s1.to_dict()
        self.assertEqual(self.s1.__class__.__name__, dict_s1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.s1)
        format = "[{}] ({}) {}".format(self.s1.__class__.__name__,
                                       self.s1.id, self.s1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_s1 = self.s1.to_dict()
        instance = State(**dict_s1)
        self.assertIsNot(self.s1, instance)
        self.assertEqual(str(self.s1), str(instance))
        self.assertFalse(instance is self.s1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.s1.updated_at
        time.sleep(0.1)
        self.s1.save()
        updated_new = self.s1.updated_at
        self.assertNotEqual(update_old, updated_new)
