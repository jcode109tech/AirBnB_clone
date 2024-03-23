#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage class"""

    def setUp(self):
        """Set up for test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean test files created"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test reload method"""
        obj = BaseModel()
        obj.save()
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
