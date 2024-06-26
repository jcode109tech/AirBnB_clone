#!/usr/bin/python3
"""
=== Amenity class : <inherites> : BaseModel
> SET AMENITY DETAILS
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    >> Custom amenity class
    :
    Public Attributes:
        name: string - empty string  - amenity name
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
