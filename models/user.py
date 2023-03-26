#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from environ import get_env


class User(BaseModel, Base):
    '''a class User that inherits from BaseModel
    ...
    Attributes
    ----------
    email : str
    password : str
    first_name : sr
    last_name : str
    '''

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', back_populates='user', cascade='delete')
    reviews = relationship('Review', back_populates='user', cascade='delete')
