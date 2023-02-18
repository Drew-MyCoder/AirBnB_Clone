#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
City module in models
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the attributes/methods for the City class, subclass of BaseModel
    Other attributes/methods are inherited from the BaseModel.
    """

    state_id = ""
    name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize the variables and methods"""
    #     super().__init__(self, *args, **kwargs
