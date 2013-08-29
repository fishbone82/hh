from pyramid.view import view_config
from base import ViewBase


@view_config(route_name='welcome', renderer='welcome.mako')
class welcome(ViewBase):
    def call(self):
        return {"ok": 1}