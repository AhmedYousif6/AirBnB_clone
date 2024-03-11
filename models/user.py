#!/usr/bin/python3
''' module for user class.'''
from base_model import BaseModel


class User(BaseModel):
    ''' class for user objects.'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
