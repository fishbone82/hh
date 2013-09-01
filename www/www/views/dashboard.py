from pyramid.view import view_config
from base import ViewBase


@view_config(route_name='dashboard', renderer='dashboard.jinja2')
class dashboard(ViewBase):
    def call(self):
        return {"ok": 1}