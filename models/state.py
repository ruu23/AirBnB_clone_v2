#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    """State class definition."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize State."""
        if 'name' not in kwargs or kwargs['name'] == "":
            raise ValueError("Name is required for State")
        super().__init__(*args, **kwargs)
