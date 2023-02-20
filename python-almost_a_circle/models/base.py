#!/usr/bin/python3
"""
Class Module
"""

import json
import os.path


class Base:
    """
    Initializing Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """ Assing the public instance attribute id"""
            self.id = id
        else:
            """
            Increment the private class
            and assing the new value to the
            public instance attribute id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method taht returns a json string representation
        """
        if list_dictionaries is None:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as fd:
            fd.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    """
    Updating the class base; by adding the method that return a list
    of the json string representation
    """
    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns  a list with the json string representation
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    """
    Updating Base class; by adding create method
    """
    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            simple_create = cls(1, 1)
        elif cls.__name__ == "Square":
            simple_create = cls(1)
        simple_create.update(**dictionary)
        return (simple_create)

    """
    Updating the base class by adding the load_from_file
    """
    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as fd:
            list_str = fd.read()
            list_cls = cls.from_json_string(list_str)
            list_to_load = []
            for i in range(len(list_cls)):
                list_to_load.append(cls.create(**list_cls[i]))
            return (list_to_load)
