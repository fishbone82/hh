from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import hosthealth as app


@view_config(route_name='login', renderer='login.mako')
def login(request):
    # trying to auth if email and password has been sent
    if 'email' in request.POST and 'password' in request.POST:
        if app.authenticate(request.POST['email'], request.POST['password']):
            #url = request.route_url('home')
            return HTTPFound(location='/')
        else:
            return {"error": "Invalid email or password", "session": request.session}
    #request.session.save()
    return {"error": None, 'project': 'HostHealth',"session": request.session}