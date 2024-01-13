#!/usr/bin/python3
"""File storage Module"""

import json
import os


class FileStorage:
    """
    File storage is a class that allows you to
        - Serialise instances
        - Desirialise instances
        - Save Objects in a JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the json file"""
        serialized_objs = {}
        for key, value in self.all().items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(serialized_objs, json_file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        dict_classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
            }
        if not os.path.isfile(FileStorage.__file_path):
            return
        deserialised_objs = {}
        with open(FileStorage.__file_path, "r", encoding="utf-8") as json_file:
            dic_json = json.load(json_file)
            for key, kwrags in dic_json.items():
                class_name, id = key.split(".")
                # copy_class_name = class_name
                # if copy_class_name == "BaseModel":
                #     copy_class_name = "Base_Model"
                # module_name = f"models.{copy_class_name.lower()}"
                # module = importlib.import_module(module_name)
                # class_obj = getattr(module, class_name)
                obj = dict_classes[class_name](**kwrags)
                deserialised_objs[key] = obj
            FileStorage.__objects = deserialised_objs
