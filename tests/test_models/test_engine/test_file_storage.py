#!/usr/bin/python3
"""Unittest for FileStorage Class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageClass(unittest.TestCase):
    """Test cases for Class FileStorage"""

    def setUp(self):
        """setUp method"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.f1 = FileStorage()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.s1 = State()
        self.r1 = Review()
        self.u1 = User()
        self.f2 = FileStorage()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.f1
        del self.a1
        del self.c1
        del self.p1
        del self.s1
        del self.r1
        del self.u1
        del self.f2
        filename = "file.json"
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test attributes for class FileStorage"""
        FileStorage._FileStorage__objects = {}
        filename = "file.json"
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all_empty(self):
        """Tests all() instance method when __objects is empty"""
        result = self.f1.all()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        # self.assertEqual(len(result), 1)

    def test_all_none_empty(self):
        """Tests all() instance method"""
        self.f1.new(self.b1)
        result = self.f1.all()
        self.assertIsInstance(result, dict)
        self.assertNotEqual(result, {})
        self.assertIs(result, self.f1._FileStorage__objects)

    def test_reload_with_all(self):
        """Tests all() with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(None)

    def test_new_with_all_classes(self):
        """Tests new() instance method with all classes"""
        self.f1.new(self.b1)
        self.f1.new(self.a1)
        self.f1.new(self.c1)
        self.f1.new(self.p1)
        self.f1.new(self.r1)
        self.f1.new(self.s1)
        self.f1.new(self.p1)
        self.f1.save()

        self.assertIn(f"{self.b1.__class__.__name__}.{self.b1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.u1.__class__.__name__}.{self.u1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.a1.__class__.__name__}.{self.a1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.c1.__class__.__name__}.{self.c1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.s1.__class__.__name__}.{self.s1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.p1.__class__.__name__}.{self.p1.id}",
                      self.f1.all().keys())

    def test_save(self):
        """Tests save() instance method with all classes"""
        self.f1.new(self.b1)
        self.f1.new(self.a1)
        self.f1.new(self.c1)
        self.f1.new(self.p1)
        self.f1.new(self.r1)
        self.f1.new(self.s1)
        self.f1.new(self.p1)
        self.f1.save()

        self.assertIn(f"{self.b1.__class__.__name__}.{self.b1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.u1.__class__.__name__}.{self.u1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.a1.__class__.__name__}.{self.a1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.c1.__class__.__name__}.{self.c1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.s1.__class__.__name__}.{self.s1.id}",
                      self.f1.all().keys())
        self.assertIn(f"{self.p1.__class__.__name__}.{self.p1.id}",
                      self.f1.all().keys())

    def test_reload(self):
        """Tests reload() instance method"""
        filename = "file.json"
        self.f2 = FileStorage()
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass
        self.f1.new(self.b1)
        self.f1.new(self.a1)
        self.f1.new(self.c1)
        self.f1.new(self.p1)
        self.f1.new(self.r1)
        self.f1.new(self.s1)
        self.f1.new(self.p1)
        self.f1.save()
        # use another instance of file storage
        self.f2.reload()
        file_objects = self.f2.all()
        # print(file_objects)

        self.assertIn(f"{self.b1.__class__.__name__}.{self.b1.id}",
                      file_objects)
        self.assertIn(f"{self.u1.__class__.__name__}.{self.u1.id}",
                      file_objects)
        self.assertIn(f"{self.a1.__class__.__name__}.{self.a1.id}",
                      file_objects)
        self.assertIn(f"{self.c1.__class__.__name__}.{self.c1.id}",
                      file_objects)
        self.assertIn(f"{self.s1.__class__.__name__}.{self.s1.id}",
                      file_objects)
        self.assertIn(f"{self.p1.__class__.__name__}.{self.p1.id}",
                      file_objects)

    def test_reload_with_None(self):
        """Tests reload with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(None)

    def test_reload_with_save(self):
        """Tests save() with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(None)
