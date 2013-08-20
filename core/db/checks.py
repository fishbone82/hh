from sqlalchemy.ext.declarative import declarative_base
import json
Base = declarative_base()
from sqlalchemy import Column, Integer, TIMESTAMP, Enum, String
from workers import Worker
from connection import Session
from sqlalchemy import text


class Check(Base):
    __tablename__ = 'checks'
    check_id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    state = Column(Enum('-1', '0', '1', '2'))
    check_interval = Column(Integer)
    next_check = Column(TIMESTAMP)
    plugin = Column(String)
    args = Column(String)
    workers = Column(String)

    def generate_token(self):
        return "G654hpx5"

    def get_workers(self):
        session = Session()
        workers_list = json.loads(self.workers)
        workers = session.query(Worker).filter(Worker.worker_id.in_(workers_list)).all()
        session.close()
        return workers

    def args_dict(self):
        args_dict = json.loads(self.args)
        args_dict['token'] = self.generate_token()
        return args_dict

    def update_next_check_time(self, results):
        print results
        session = Session()
        self.next_check = text('NOW() + INTERVAL check_interval SECOND')
        self.state = 0  # -1 = active but never checked, 0 = active and checked 1 = disabled
        session.merge(self)
        session.flush()
        session.close()

    # def __init__(self, host_id, state,  plugin,  next_check=None, check_interval=600):
    #     self.host_id = host_id
    #     self.plugin = plugin
    #     self.state = state
    #     self.check_interval = check_interval
    #     self.next_check = next_check
