#!/usr/bin/python3
"""
=== City class : <inherites> : BaseModel
> SET REVIEW DETAILS
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    :
    Public Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): The text of the review

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")