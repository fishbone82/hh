from checks import Check
from connection import Session
session = Session()

check = session.query(Check).filter(Check.check_id == 2).all()
print check

