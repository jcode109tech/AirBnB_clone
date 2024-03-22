#!/usr/bin/python3
"""
Class <base_model>
Defines all common attributes/ methods for other classes
"""


import uuid
from datetime import datetime
import models 


class BaseModel:
    """
        Basemodel <class> {creating and maaging instatnces}
    """
    FORMAT_TIME = "%Y-%m-%dT%H:%M:%S.%f"
    
    def __init__(self, *args, **kwargs):
        """
           Initialize : Base model
           ARGS:
           > *args - list of input / values
           > **kwargs - dictonary input / values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, self.FORMAT_TIME)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ BaseClass documentation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    
    def save(self):
        """
            Updates on every crud operation
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        

    def to_dict(self) -> dict:
        """
            Return a dictionary of instance attributes.
        """
        new_instances = ['name', 'my_number']
        # data = {k: v for k, v in self.__dict__.items() if k not in Other_instances}
        data = {}  # Initialize an empty dictionary to store the extracted data
        for new_key, new_value in self.__dict__.items():  # Iterate over each key-value pair in the object's __dict__
            if new_key not in new_instances:  # Check if the key is not in the Other_instances list
                data[new_key] = new_value  # Add the key-value pair to the data dictionary if the key is not in Other_instances
        data['__class__'] = self.__class__.__name__
        for new_key, new_value in data.items():
            if isinstance(new_value, datetime):
                data[new_key] = new_value.isoformat()
        return data
