# Mysql section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
mysql_engine = create_engine('mysql://orthus:ordbpass@fishbone.homelinux.org/orthus', echo=False)
Session = sessionmaker(bind=mysql_engine)

# Mongo section
from pymongo import Connection
mongo_connection = Connection('fishbone.homelinux.org', 27017)
Mongo = mongo_connection.orthus_checks
Mongo.authenticate('orthus', 'ormongopass')

# ORM section
from sqlalchemy.ext.declarative import declarative_base
ORMBase = declarative_base()


def get_rotten_checks():
    from checks import Check as CheckClass
    session = Session()
    rotten_checks = session.query(CheckClass).filter("next_check<now()").options(joinedload('host')).all()
    session.close()
    return rotten_checks
