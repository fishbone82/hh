from pyramid.view import view_config
from base import ViewBase
from orthus.db import Session
from orthus.db.hosts import Host
from orthus.db.checks import Check


@view_config(route_name='hosts', renderer='hosts.jinja2')
class hosts(ViewBase):
    def call(self):
        session = Session()
        user = session.merge(self.request.session['user'])
        return { "hosts": user.hosts }