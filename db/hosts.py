from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from orthus.db import ORMBase


class Host(ORMBase):
    __tablename__ = 'hosts'
    host_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    address = Column(String)
    checks = relationship('Check', backref="host")
