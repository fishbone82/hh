from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from orthus.db import ORMBase


class User(ORMBase):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    hosts = relationship('Host', backref="user")