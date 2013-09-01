from pyramid.view import view_config
from base import ViewBase
from orthus.db import Session
from orthus.db.hosts import Host

@view_config(route_name='hosts', renderer='hosts.jinja2')
class hosts(ViewBase):
    def call(self):
        session = Session()
        hosts = session.query(Host).filter(Host.user_id == self.request.session.user.user_id).all()
        return { "hosts": hosts }