#!/usr/bin/python3
"""Unittest for FileStorage Class"""


from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import unittest


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
        """Teardown method for class FileManger"""
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

    def test_None_file_storage(self):
        """Test by passing None to filestorage"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_attributes(self):
        """Test attributes for class FileStorage"""
        filename = "file.json"
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_initial_values(self):
        """Test initial values for FileStorage class attributes"""
        FileStorage._FileStorage__objects = {}
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_empty(self):
        """Tests all() instance method when __objects is empty"""
        FileStorage._FileStorage__objects = {}
        result = self.f1.all()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(self.f1.all(), {})

    def test_all_none_empty(self):
        """Tests all() instance method"""
        self.f1.new(self.b1)
        result = self.f1.all()
        self.assertIsInstance(result, dict)
        self.assertNotEqual(result, {})
        self.assertIs(result, self.f1._FileStorage__objects)

    def test_all_with_None(self):
        """Tests all() with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(None)

    def test_all_argument_str(self):
        """Tests all() instance method with string as argument"""
        with self.assertRaises(TypeError):
            self.f1.all("None")

    def test_all_argument_list(self):
        """Tests all() instance method with list as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(["town"])

    def test_all_argument_int(self):
        """Tests all() instance method with integer as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(1994)

    def test_all_argument_float(self):
        """Tests all() instance method with float as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(19.94)

    def test_all_argument_tuple(self):
        """Tests all() instance method with tuple as argument"""
        with self.assertRaises(TypeError):
            self.f1.all((19, 94))

    def test_all_argument_dict(self):
        """Tests all() instance method with dictionary as argument"""
        with self.assertRaises(TypeError):
            self.f1.all({})

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

    def test_new_None_argument(self):
        """Tests new() instance method with None as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new(None)

    def test_new_argument_str(self):
        """Tests new() instance method with string as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new("None")

    def test_new_argument_list(self):
        """Tests new() instance method with list as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new(["town"])

    def test_new_argument_int(self):
        """Tests new() instance method with integer as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new(1994)

    def test_new_argument_float(self):
        """Tests new() instance method with float as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new(19.94)

    def test_new_argument_tuple(self):
        """Tests new() instance method with tuple as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new((19, 94))

    def test_new_argument_dict(self):
        """Tests new() instance method with dictionary as argument"""
        with self.assertRaises(AttributeError):
            self.f1.new({})

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

    def test_reload_multiple_args(self):
        """Tests reload() with multiple as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(None, None)
            self.f1.reload("None", "None")
            self.f1.reload(12, 32)
            self.f1.reload(1.2, 4.5)
            self.f1.reload((1, 2), (3, 5))
            self.f1.reload({}, {})

    def test_new_multiple_args(self):
        """Tests new() with multiple as argument"""
        with self.assertRaises(TypeError):
            self.f1.new(None, None)
            self.f1.new("None", "None")
            self.f1.new(12, 32)
            self.f1.new(1.2, 4.5)
            self.f1.new((1, 2), (3, 5))
            self.f1.new({}, {})

    def test_all_multiple_args(self):
        """Tests all() with multiple as argument"""
        with self.assertRaises(TypeError):
            self.f1.all(None, None)
            self.f1.all("None", "None")
            self.f1.all(12, 32)
            self.f1.all(1.2, 4.5)
            self.f1.all((1, 2), (3, 5))
            self.f1.all({}, {})

    def test_save_multiple_args(self):
        """Tests save() with multiple as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(None, None)
            self.f1.save("None", "None")
            self.f1.save(12, 32)
            self.f1.save(1.2, 4.5)
            self.f1.save((1, 2), (3, 5))
            self.f1.save({}, {})

    def test_save_None_argument(self):
        """Tests save() with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(None)

    def test_save_argument_str(self):
        """Tests save() instance method with string as argument"""
        with self.assertRaises(TypeError):
            self.f1.save("None")

    def test_save_argument_list(self):
        """Tests save() instance method with list as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(["town"])

    def test_save_argument_int(self):
        """Tests save() instance method with integer as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(1994)

    def test_save_argument_float(self):
        """Tests save() instance method with float as argument"""
        with self.assertRaises(TypeError):
            self.f1.save(19.94)

    def test_save_argument_tuple(self):
        """Tests save() instance method with tuple as argument"""
        with self.assertRaises(TypeError):
            self.f1.save((19, 94))

    def test_save_argument_dict(self):
        """Tests reload() instance method with dictionary as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload({})

    def test_reload_None_argument(self):
        """Tests reload() with None as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(None)

    def test_reload_argument_str(self):
        """Tests reload() instance method with string as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload("None")

    def test_reload_argument_list(self):
        """Tests reload() instance method with list as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(["town"])

    def test_reload_argument_int(self):
        """Tests reload() instance method with integer as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(1994)

    def test_reload_argument_float(self):
        """Tests reload() instance method with float as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload(19.94)

    def test_reload_argument_tuple(self):
        """Tests reload() instance method with tuple as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload((19, 94))

    def test_reload_argument_dict(self):
        """Tests reload() instance method with dictionary as argument"""
        with self.assertRaises(TypeError):
            self.f1.reload({})

    def test_initialization_without_args(self):
        """Tests for class FileStorage initialization without args"""
        with self.assertRaises(TypeError):
            FileStorage(None)
            FileStorage("Test")

    def test_file_path(self):
        """Tets for the type of the class attribute file_path"""

        file_path = FileStorage._FileStorage__file_path
        self.assertEqual(type(file_path), str)
        self.assertFalse(hasattr(self.f2, '__file_path'))
        self.assertEqual(file_path, "file.json")

    def test_objects(self):
        """Tets for class attribute objects"""

        objects = FileStorage._FileStorage__objects
        result = self.f2.all()
        self.assertEqual(type(objects), dict)
        self.assertFalse(hasattr(self.f2, '__objects'))
        self.assertEqual(result, objects)

    def test_all(self):
        """Defines all test cases for the intance method all()"""
        objects = FileStorage._FileStorage__objects
        result = self.f2.all()
        self.assertEqual(type(result), dict)
        self.assertEqual(result, objects)

    def test_all_returns_empty_dict(self):
        """Tests all returns empty dictionary"""
        FileStorage._FileStorage__objects = {}
        result = self.f2.all()
        self.assertEqual(result, {})

    def test_all_args(self):
        """Defines tests for all with args"""
        with self.assertRaises(TypeError):
            self.f2.all("test")
            self.f2.all("test", "test")
            self.f2.all(None)

    def test_new(self):
        """Tests new adds object to the objects attribute"""

        self.f2.new(self.b1)
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.b1.id, objects.keys())
        self.assertIn(self.b1, objects.values())

    def test_new_arg(self):
        """Tests new raises type error with wrong args"""
        with self.assertRaises(TypeError):
            self.f2.new()

    def test_new_invalid_args(self):
        """Tests for invalid args used with new method of class FileStorage"""
        with self.assertRaises(AttributeError):
            self.f2.new("")
            self.f2.new(None, None)

    def test_save(self):
        """Defines all edge case tests for the method save()"""

        self.f2.new(self.b1)

        self.f2.save()
        bm_key = "BaseModel." + self.b1.id

        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn(bm_key, data.keys())

    def test_save_args(self):
        """Tests whether save accepts arguments"""

        with self.assertRaises(TypeError):
            self.f2.save("Test")
            self.f2.save("Test", "Test")
            self.f2.save(None)

    def test_reload_args(self):
        """Tests reload args"""
        with self.assertRaises(TypeError):
            self.f2.reload("")
            self.f2.reload(None)
            self.f2.reload(int)

    def test_reload_file_missing(self):
        """Tests reload when file is missing"""
        try:
            os.remove("file.json")
        except (FileNotFoundError):
            pass
        try:
            self.f2.reload()
        except Exception as e:
            self.fail()


if __name__ == "__main__":
    unittest.main()
