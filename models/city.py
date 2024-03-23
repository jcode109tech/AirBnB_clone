#!/usr/bin/python3
"""
=== City class : <inherites> : BaseModel
> SET CITY DETAILS
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    >> Custom city class
    :
    Public Attributes:
        state_id: string - empty string - The state id.
        name: string - empty string - The name of the city

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
