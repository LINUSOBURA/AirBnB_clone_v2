#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel

#from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenities in the house"""
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        #place_amenity = relationship('Place', secondary=place_amenity)
    else:
        name = ""
