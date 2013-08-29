from pyramid.view import view_config


@view_config(route_name='welcome', renderer='welcome.mako')
def welcome(request):
    return {'project': 'HostHealth', 'page_title': 'HostHealth::Welcome'}