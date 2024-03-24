#!/usr/bin/python3
"""
=== City class : <inherites> : BaseModel
> SET CITY DETAILS
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    >> Custom city class
    :
    Public Attributes:
        name (str): The name of the state

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
