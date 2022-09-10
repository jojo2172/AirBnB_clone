#!/usr/bin/python3
""" User Model """
from models.base_model import BaseModel


class User(BaseModel):
    """User information"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
