#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class with attributes inherited from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
