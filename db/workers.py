from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, TIMESTAMP, Enum, String


class Worker(Base):
    __tablename__ = 'workers'
    worker_id = Column(Integer, primary_key=True)
    address = Column(String)
    location = Column(String)
