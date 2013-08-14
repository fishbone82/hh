from core import db

session = db.Session()

for instance in session.query(db.Checks).order_by(db.Checks.check_id):
    print instance.args

for row in session.query(db.Checks).all():
    print row.next_check