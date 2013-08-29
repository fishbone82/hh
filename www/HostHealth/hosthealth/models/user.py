from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from __init__ import ORMBase


class User(ORMBase):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    #checks = relationship('Check', backref="host")