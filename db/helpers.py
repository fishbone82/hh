from orthus.db import Session
from orthus.db.checks import Check
from orthus.db.hosts import Host
from sqlalchemy.orm import joinedload

def get_rotten_checks():
    s = Session()
    rotten_checks = s.query(Check).filter("next_check<now()").options(joinedload('host')).all()
    return rotten_checks