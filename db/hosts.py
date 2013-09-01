from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from orthus.db import ORMBase


class Host(ORMBase):
    __tablename__ = 'hosts'
    host_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    address = Column(String)
    checks = relationship('Check', backref="host")
