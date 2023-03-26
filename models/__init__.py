#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from environ import get_env
from .state import State
from .amenity import Amenity
from .base_model import BaseModel, Base
from .city import City
from .place import Place
from .review import Review
from .user import User

if get_env('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

elif get_env('HBNB_TYPE_STORAGE') == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
