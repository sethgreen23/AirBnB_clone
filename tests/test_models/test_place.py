#!/usr/bin/python3
"""Unittest for class Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import time


class TestPlaceClass(unittest.TestCase):
    """Unittest class for testing class Place
    Test the following attributes
    - email = ""
    - password = ""
    - first_name = ""
    - last_name = ""
"""
    def setUp(self):
        """setUp method"""
        self.p1 = Place()
        self.p2 = Place()
        # dict_storage = storage.all()
        # dict_storage = {}

    def tearDown(self):
        """tearDown method"""
        del self.p1
        del self.p2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_Place_id(self):
        """Test Place instance id"""
        self.assertNotEqual(self.p1.id, self.p2.id)

    # ***************************************************************
    def test_Place_city_id(self):
        """Test Place city id"""
        self.assertIsInstance(self.p1.city_id, str)
        self.p1.city_id = "ET.AA"
        self.assertEqual(self.p1.city_id, "ET.AA")

    def test_Place_name(self):
        """Test Place name"""
        self.assertIsInstance(self.p1.name, str)
        self.p1.name = "Fridge"
        self.assertEqual(self.p1.name, "Fridge")

    def test_Place_user_id(self):
        """Test Place user_id"""
        self.assertIsInstance(self.p1.user_id, str)
        self.p1.user_id = "rock9"
        self.assertEqual(self.p1.user_id, "rock9")

    def test_Place_description(self):
        """Test Place description"""
        self.assertIsInstance(self.p1.description, str)
        self.p1.description = "Cosy place"
        self.assertEqual(self.p1.description, "Cosy place")

    def test_Place_number_rooms(self):
        """Test Place number_rooms"""
        self.assertIsInstance(self.p1.number_rooms, int)
        self.p1.number_rooms = 5
        self.assertEqual(self.p1.number_rooms, 5)

    def test_Place_number_bathrooms(self):
        """Test Place number_bathrooms"""
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.p1.number_bathrooms = 2
        self.assertEqual(self.p1.number_bathrooms, 2)

    def test_Place_max_guest(self):
        """Test Place name"""
        self.assertIsInstance(self.p1.max_guest, int)
        self.p1.max_guest = 5
        self.assertEqual(self.p1.max_guest, 5)

    def test_Place_price_by_night(self):
        """Test Place price_by_night"""
        self.assertIsInstance(self.p1.price_by_night, int)
        self.p1.price_by_night = 23
        self.assertEqual(self.p1.price_by_night, 23)

    def test_Place_latitude(self):
        """Test Place latitude"""
        self.assertIsInstance(self.p1.latitude, float)
        self.p1.latitude = 123.23
        self.assertEqual(self.p1.latitude, 123.23)

    def test_Place_longitude(self):
        """Test Place longitude"""
        self.assertIsInstance(self.p1.longitude, float)
        self.p1.longitude = 25.23
        self.assertEqual(self.p1.longitude, 25.23)

    def test_Place_amenity_ids(self):
        """Test Place amenity_ids"""
        amenity_ids = ["Fridge", "Stove", "TV", "WIFI"]
        self.assertIsInstance(self.p1.amenity_ids, list)
        self.p1.amenity_ids = ["Fridge", "Stove", "TV", "WIFI"]
        self.assertEqual(self.p1.amenity_ids, amenity_ids)

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.p1.created_at, datetime)
        self.assertIsInstance(self.p1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for Place class attributes"""
        self.assertEqual(self.p1.name, "")

    def test_Place_inherits_BaseModel(self):
        """Test if Place inherits from BaseModel"""
        self.assertIsInstance(self.p1, BaseModel)

    def test_Place_type(self):
        """Test if Place instance is of the same type"""
        self.assertEqual(type(self.p1), Place)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.p1.__class__.__name__}.{self.p1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.p2.__class__.__name__}.{self.p2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.p1.save()
        self.p2.save()

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_p1 = self.p1.to_dict()
        self.assertIsInstance(dict_p1, dict)
        self.assertIn('id', dict_p1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_p1 = self.p1.to_dict()
        self.assertIsInstance(dict_p1, dict)
        self.assertIn('created_at', dict_p1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_p1 = self.p1.to_dict()
        self.assertIsInstance(dict_p1, dict)
        self.assertIn('updated_at', dict_p1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_p1 = self.p1.to_dict()
        self.assertEqual(self.p1.__class__.__name__, dict_p1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.p1)
        format = "[{}] ({}) {}".format(self.p1.__class__.__name__,
                                       self.p1.id, self.p1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_p1 = self.p1.to_dict()
        instance = Place(**dict_p1)
        self.assertIsNot(self.p1, instance)
        self.assertEqual(str(self.p1), str(instance))
        self.assertFalse(instance is self.p1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.p1.updated_at
        time.sleep(0.1)
        self.p1.save()
        updated_new = self.p1.updated_at
        self.assertNotEqual(update_old, updated_new)
