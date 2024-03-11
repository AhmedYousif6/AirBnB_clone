#!/usr/bin/python3
""" Contain the class (base class) that defines all common attributes
and methods for other classes."""

from uuid import uuid4
from datetime import datetime
from engine import storage

class BaseModel:
    """ The base class for other classes.
    Args:
        *args: list of arguments.
        **kwargs: keyworded arguments.
    """

    def __init__(self, *args, **kwargs):
        """ Initialize attributes: uuid, dates when
        class was created/updated."""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, \
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ Returns a str represntation of an instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all
        keys/values of __dict__ of the instance."""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
