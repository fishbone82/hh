# import checks
# import workers
# Checks = checks.Check
# Workers = workers.Worker

# from connection import Session, Mongo
# get_session = Session
# get_mongo = Mongo


# Mysql section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_engine = create_engine('mysql://hh:hhdbpass@fishbone.me/hh', echo=False)
Session = sessionmaker(bind=db_engine)

# Mongo section
from pymongo import Connection
Mongo = Connection('fishbone.me', 27017)


# ORM section
from sqlalchemy.ext.declarative import declarative_base
ORMBase = declarative_base()