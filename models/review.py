#!/usr/bin/python3
"""Module that defines class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines class Review"""
    place_id = ""
    user_id = ""
    text = ""
