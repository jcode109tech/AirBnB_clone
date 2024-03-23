#!/usr/bin/python3
"""
Class FileStorage <inherites> from <Basemodel>
FILE: SERILIZATION AND DESERILIZATION
"""


import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
        file storage:
        private class attributes:
            __file_path: file path
            __object: dict
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns : <object>
        """
        return self.__objects

    def new(self, obj):
        """
        creates : <new object>
        """
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """
        save : <serialized> data object
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
            <Desirialize> : Json file to object
        """
        # try:
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                deserialized_data = json.load(file)
                for key, value in deserialized_data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        # except FileNotFoundError:
        #     pass
