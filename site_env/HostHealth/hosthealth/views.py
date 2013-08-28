from pyramid.view import view_config
import urlparse

@view_config(route_name='welcome', renderer='welcome.mako')
def welcome(request):
    return {'project': 'HostHealth', 'page_title': 'HostHealth::Welcome'}


@view_config(route_name='login', renderer='login.mako')
def login(request):
    query = urlparse.parse_qs(request.query_string)
    for (k, v) in query.items():
        query[k] = v[0]

    return {'project': 'HostHealth', 'page_title': 'HostHealth::Login'}
