from pyramid.view import view_config
from base import ViewBase


@view_config(route_name='hosts', renderer='hosts.jinja2')
class welcome(ViewBase):
    def call(self):
        return {"ok": 1}