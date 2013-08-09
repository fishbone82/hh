from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, TIMESTAMP, Enum, String


class Check(Base):
    __tablename__ = 'checks'
    check_id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    state = Column(Enum('-1', '0', '1', '2'))
    plugin = Column(String)
    check_interval = Column(Integer)
    next_check = Column(TIMESTAMP)

    def __init__(self, host_id, state,  plugin,  next_check=None, check_interval=600):
        self.host_id = host_id
        self.plugin = plugin
        self.state = state
        self.check_interval = check_interval
        self.next_check = next_check
