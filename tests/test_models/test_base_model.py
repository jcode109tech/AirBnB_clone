#!/usr/bin/python3
"""
TEST FOR FILLE STORAGE
======================
"""

# import unittest
# from models.base_model import BaseModel
# from datetime import datetime
# import uuid
# from unittest.mock import patch
 

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        kwargs = {
            "id": "2dd6ef5c-467c-4f82-9521-a772ea7d84e9",
            "name": "Test",
            "value": 10,
            "created_at": "2024-03-22 12:00:00",
            "updated_at": "2024-03-22 13:00:00"
        }
        my_class = BaseModel()
        obj = my_class(**kwargs)
        self.assertEqual(obj.id, "2dd6ef5c-467c-4f82-9521-a772ea7d84e9")
        self.assertEqual(obj.name, "Test")
        self.assertEqual(obj.value, 10)
        self.assertEqual(obj.created_at, datetime(2024, 3, 22, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2024, 3, 22, 13, 0, 0))

    def test_init_without_kwargs(self):
        my_class = BaseModel()
        obj =my_class()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertLessEqual(obj.created_at, datetime.now())
        self.assertLessEqual(obj.updated_at, datetime.now())
        self.assertEqual(obj.created_at, obj.updated_at)

if __name__ == '__main__':
    unittest.main()









    # def test_attributes(self):
    #     """
    #     Test that the instance attributes are set correctly.
    #     """
    #     my_model = BaseModel()
    #     self.assertTrue(hasattr(my_model, "id"))
    #     self.assertTrue(hasattr(my_model, "created_at"))
    #     self.assertTrue(hasattr(my_model, "updated_at"))
    #     self.assertIsInstance(my_model.id, str)
    #     self.assertIsInstance(my_model.created_at, datetime.datetime)
    #     self.assertIsInstance(my_model.updated_at, datetime.datetime)

    # def test_str_representation(self):
    #     """
    #     Test the string representation of the BaseModel instance.
    #     """
    #     my_model = BaseModel()
    #     str_rep = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
    #     self.assertEqual(str(my_model), str_rep)

    # def test_save_method(self):
    #     """
    #     Test the save method of the BaseModel instance.
    #     """
    #     my_model = BaseModel()
    #     old_updated_at = my_model.updated_at
    #     my_model.save()
    #     new_updated_at = my_model.updated_at
    #     self.assertNotEqual(old_updated_at, new_updated_at)

    # def test_to_dict_method(self):
    #     """
    #     Test the to_dict method of the BaseModel instance.
    #     """
    #     my_model = BaseModel()
    #     my_model_dict = my_model.to_dict()
    #     self.assertIsInstance(my_model_dict, dict)
    #     self.assertEqual(my_model_dict["__class__"], "BaseModel")
    #     self.assertEqual(type(my_model_dict["created_at"]), str)
    #     self.assertEqual(type(my_model_dict["updated_at"]), str)
    #     self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
    #     self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())


# if __name__ == "__main__":
#     unittest.main()


