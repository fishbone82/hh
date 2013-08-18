# Mysql section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_engine = create_engine('mysql://hh:hhdbpass@fishbone.me/hh', echo=False)
Session = sessionmaker(bind=db_engine)

# Mongo section
from pymongo import Connection
connection = Connection('fishbone.me', 27017)

