#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a specific class"""
        if cls:
            return {obj.id: obj for obj in self.__session.query(cls).all()}
        else:
            all_objs = {}
            for cls_name in ['State', 'City']:
                all_objs.update(self.all(eval(cls_name)))
            return all_objs

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Reload the session from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

