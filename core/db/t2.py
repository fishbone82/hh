from __init__ import Session, Mongo
from checks import Check
session = Session()

from sqlalchemy import text

check = session.query(Check).filter(Check.check_id == 2).first()
print "check: %s host: %s time: %s" % (check.check_id, check.host_id, check.next_check)

print check.host.address
print check.get_mongo_collection()
print check.get_workers()
check.next_check = text('now() + INTERVAL check_interval second')
session2 = Session()

session2.merge(check)

print session2.dirty
session2.commit()

mongo = Mongo
collection = getattr(mongo, 'user_1')
collection.insert({"foo": "bar", "bar": "baz"})
data = collection.find_one({"foo": "bar"})
print data
collection.remove(data)





