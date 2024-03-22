#!/usr/bin/python3
"""
=== user class : <inherites : BaseModel>
> SET USER DETAILS
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    >> Custom user details
    :
    Public Attributes:
        email: string - empty string - email@.com
        password: string - empty string - password
        first_name: string - empty string - first name
        last_name: string - empty string - last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
