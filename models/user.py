#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the attributes/methods for the User class, subclass of BaseModel
    Other attributes/methods are inherited from the BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize the variables and methods"""
    #     super().__init__(self, *args, **kwargs)
