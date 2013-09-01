# Mysql section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
mysql_engine = create_engine('mysql://orthus:ordbpass@fishbone.me/orthus', echo=False)
Session = sessionmaker(bind=mysql_engine)

# Mongo section
from pymongo import Connection
mongo_connection = Connection('fishbone.homelinux.org', 27017)
Mongo = mongo_connection.orthus_checks
Mongo.authenticate('orthus', 'ormongopass')

# ORM section
from sqlalchemy.ext.declarative import declarative_base
ORMBase = declarative_base()

