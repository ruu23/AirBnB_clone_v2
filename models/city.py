#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """City class definition."""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """Initialize City."""
        if 'name' not in kwargs or kwargs['name'] == "":
            raise ValueError("Name is required for City")
        if 'state_id' not in kwargs or kwargs['state_id'] == "":
            raise ValueError("state_id is required for City")
        super().__init__(*args, **kwargs)
