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
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    if models.storage_type != 'db':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances."""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

