#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

class DBStorage:
    """Database storage engine for MySQL using SQLAlchemy."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for cls_name in ['User', 'State', 'City', 'Amenity', 'Place', 'Review']:
                objs.extend(self.__session.query(eval(cls_name)).all())
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the session."""
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

