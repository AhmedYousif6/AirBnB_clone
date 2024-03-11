#!/usr/bin/python3
''' FileStorage class to serialize and deserialize
json file.'''

import datetime
import json
import os


class FileStorage:
    ''' serializes instances to a JSON file and
    deserializes JSON file to instances.
    Attributes:
        __file_path: path of the json file.
        __objects: dictionary to store objects by class name and id.'''
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def all(self):
        ''' Return all objects with class name and id.'''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets class name and id of obj as key in
        __objects and obj as value.'''
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        ''' serialize objects to json file.'''
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        ''' deserialize json file to objects if its exist.'''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
