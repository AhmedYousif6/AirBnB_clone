#!/usr/bin/python3
''' module for review class.'''
from base_model import BaseModel


class Review(BaseModel):
    ''' class for review objects.'''
    place_id = ""
    user_id = ""
    text = ""
