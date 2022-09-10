#!/usr/bin/python3
"""
Review Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review of the place"""
    place_id = ''
    user_id = ''
    text = ''
