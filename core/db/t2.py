from checks import Check
from connection import Session, Mongo
session = Session()

from sqlalchemy import text

check = session.query(Check).filter(Check.check_id == 2).first()
print "check: %s host: %s time: %s" % (check.check_id, check.host_id, check.next_check)

check.next_check = text('now() + check_interval')
session2 = Session()

session2.merge(check)
print session2.dirty
session2.commit()

mongo = Mongo
db = mongo.mydb
collection = db.TestData
collection.insert({"foo": "bar", "bar": "baz"})
data = collection.find_one({"foo": "bar"})
print data
collection.remove(data)
