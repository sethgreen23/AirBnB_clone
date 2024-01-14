#!/usr/bin/python3
"""Unittest for the BaseModel"""

from datetime import datetime
from models import storage
from models.base_model import BaseModel
import time
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class
    """

    def setUp(self):
        """setUp method for base_model test
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """tearDown method for base_model test
        """
        del self.b1
        del self.b2

    def test_init_None(self):
        """Test __init__ with None argument"""
        self.b3 = BaseModel(None)
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_init_list(self):
        """Test __init__ with list argument"""
        self.b3 = BaseModel(["Dog", 12, 33.3, (1, 2), {"first_name": "Seth"}])
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_init_str(self):
        """Test __init__ with str argument"""
        self.b3 = BaseModel("Dog")
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_init_int(self):
        """Test __init__ with int argument"""
        self.b3 = BaseModel(33)
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_init_tuple(self):
        """Test __init__ with tuple argument"""
        self.b3 = BaseModel((33, 32))
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_init_float(self):
        """Test __init__ with list argument"""
        self.b3 = BaseModel(33.3)
        self.b3.save()
        result = self.b3.to_dict()

        self.assertTrue("updated_at" in result.keys())
        self.assertTrue("id" in result.keys())
        self.assertTrue("__class__" in result.keys())
        self.assertTrue("created_at" in result.keys())
        self.assertEqual(len(result), 4)

    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b2.updated_at, datetime)

    def test_id(self):
        """Testing the uuid"""
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b1.id, str)

    def test_created_at(self):
        """Testing created_at"""
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertIsInstance(self.b1.created_at, datetime)

    def test_updated_at(self):
        """Testing updated_at"""

        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_created_at_updated_at(self):
        """Testing dates"""
        self.assertNotEqual(self.b1.created_at, self.b2.created_at)
        self.assertNotEqual(self.b1.updated_at, self.b2.updated_at)

    def test_save_updated_at(self):
        """Testing save with created_at and updated_at"""
        self.b4 = BaseModel()
        updated_old = self.b4.updated_at
        created = self.b4.created_at
        time.sleep(0.1)
        self.b4.save()
        updated_new = self.b4.updated_at
        self.assertNotEqual(updated_old, updated_new)
        self.assertEqual(self.b4.created_at, created)

    def test_to_dict(self):
        """Testing to_dict"""
        d = self.b1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_str(self):
        """Testing str"""
        str_rep = str(self.b1)
        self.assertIn("BaseModel", str_rep)
        self.assertIn(self.b1.id, str_rep)
        # order preserving
        cls_rp = str(self.b1)
        self.assertIn(str(self.b1.__dict__), str_rep)
        format = "[{}] ({}) {}".format(self.b1.__class__.__name__,
                                       self.b1.id, self.b1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_init_from_dict(self):
        """
        Testing the creation of instance from a dictionary
        """
        self.b1.name = "My_First_Model"
        self.b1.my_number = 89
        dict_json = self.b1.to_dict()
        b1_clone = BaseModel(**dict_json)
        self.assertTrue(hasattr(b1_clone, "id"))
        self.assertTrue(hasattr(b1_clone, "created_at"))
        self.assertTrue(hasattr(b1_clone, "updated_at"))
        self.assertTrue(hasattr(b1_clone, "name"))
        self.assertTrue(hasattr(b1_clone, "my_number"))
        self.assertEqual(self.b1.id, b1_clone.id)
        self.assertEqual(self.b1.created_at, b1_clone.created_at)
        self.assertEqual(self.b1.updated_at, b1_clone.updated_at)
        self.assertEqual(self.b1.name, b1_clone.name)
        self.assertEqual(self.b1.my_number, b1_clone.my_number)
        self.assertEqual(str(self.b1.to_dict()), str(b1_clone.to_dict()))
        self.assertIsInstance(b1_clone, BaseModel)
        self.assertIsNot(b1_clone, self.b1)

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_b1 = self.b1.to_dict()
        self.assertIsInstance(dict_b1, dict)
        self.assertIn('id', dict_b1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_b1 = self.b1.to_dict()
        self.assertIsInstance(dict_b1, dict)
        self.assertIn('created_at', dict_b1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_b1 = self.b1.to_dict()
        self.assertIsInstance(dict_b1, dict)
        self.assertIn('updated_at', dict_b1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_b1 = self.b1.to_dict()
        self.assertEqual(self.b1.__class__.__name__, dict_b1["__class__"])

    def test_save(self):
        """Test save() method from FileStorage Class in BaseModel class"""
        update_1 = self.b1.updated_at
        self.b1.save()
        update_2 = self.b1.updated_at
        self.assertNotEqual(update_1, update_2)

    def test_user_type(self):
        """Test if User instance is of the same type"""
        self.assertEqual(type(self.b1), BaseModel)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.b1.__class__.__name__}.{self.b1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.b2.__class__.__name__}.{self.b2.id}"
        self.assertTrue(search_key in storage.all().keys())
        self.b1.save()
        self.b2.save()

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.b1.updated_at
        time.sleep(0.1)
        self.b1.save()
        updated_new = self.b1.updated_at
        self.assertNotEqual(update_old, updated_new)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_u1 = self.b1.to_dict()
        instance = BaseModel(**dict_u1)
        self.assertIsNot(self.b1, instance)
        self.assertEqual(str(self.b1), str(instance))
        self.assertFalse(instance is self.b1)


if __name__ == "__main__":
    unittest.main()
