#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
Amenity module in models
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the attributes/methods for the Amenity class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel.
    """

    name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs
