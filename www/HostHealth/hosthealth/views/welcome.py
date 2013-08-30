from pyramid.view import view_config
from base import ViewBase
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='welcome', renderer='welcome.jinja2')
class welcome(ViewBase):
    def call(self):
        if 'user_id' in self.request.session:
            return HTTPFound(location='/dashboard')
        return {"ok": 1}