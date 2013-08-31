from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from base import ViewBase
from hosthealth import authenticate

@view_config(route_name='login', renderer='login.jinja2')
class login(ViewBase):
    need_auth = 0

    def call(self):
        req = self.request
        # trying to auth if email and password has been sent
        if 'form_submitted' in req.POST:
            if authenticate(req.POST['email'], req.POST['password']):
                return HTTPFound(location='/')
            else:
                return {"error": "Invalid email or password"}
        return {}


@view_config(route_name='logout')
class logout(ViewBase):
    def call(self):
        self.request.session.invalidate()
        return HTTPFound(location='/')