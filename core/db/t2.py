#from __init__ import Session, Mongo
from __init__ import get_rotten_checks
print get_rotten_checks()

#session = Session()

# from sqlalchemy import text
# from sqlalchemy.orm import joinedload
#
# check = session.query(Check).filter(Check.check_id == 2).first()
# print "check: %s host: %s time: %s" % (check.check_id, check.host_id, check.next_check)
#
# #print check.host.address
# #print check.get_mongo_collection()
# print check.get_workers()
# check.next_check = text('now() + INTERVAL check_interval second')
# session2 = Session()
#
# session2.merge(check)
#
# print session2.dirty
# session2.commit()
#
# mongo = Mongo
# collection = getattr(mongo, 'user_1')
# collection.insert({"foo": "bar", "bar": "baz"})
# data = collection.find_one({"foo": "bar"})
# print data
# collection.remove(data)
#

# def print_address(check):
#     print check.host.address
#     print check.get_workers()
#
#
# def get_check():
#     session3 = Session()
#     my_check = session3.query(Check).options(joinedload('host')).first()
#     session3.close()
#     return my_check
#
# print_address(get_check())


