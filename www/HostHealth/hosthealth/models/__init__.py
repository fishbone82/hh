# Mysql section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
mysql_engine = create_engine('mysql://orthus:ordbpass@fishbone.homelinux.org/orthus', echo=False)
Session = sessionmaker(bind=mysql_engine)

# ORM section
from sqlalchemy.ext.declarative import declarative_base
ORMBase = declarative_base()