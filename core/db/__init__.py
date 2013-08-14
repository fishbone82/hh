from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import checks

Checks = checks.Check

# DB connection
db_engine = create_engine('mysql://hh:hhdbpass@fishbone.me/hh', echo=False)

Session = sessionmaker(bind=db_engine)