from pyramid.view import view_config
from base import ViewBase
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='welcome', renderer='welcome.jinja2')
class welcome(ViewBase):
    need_auth = 0

    def call(self):
        if 'user' in self.request.session:
            return HTTPFound(location='/dashboard')
        return {"ok": 1}