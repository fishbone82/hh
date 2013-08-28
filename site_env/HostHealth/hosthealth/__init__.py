from pyramid.config import Configurator
from pyramid_beaker import BeakerSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Sessions here
    config.include("pyramid_beaker")
    session_factory = BeakerSessionFactoryConfig(
        type='file',
        #key='qwerty',
        #secret='g43ger',
        data_dir='/tmp/hh/sessions/data',
        data_lock_dir='/tmp/hh/sessions/lock'
    )
    config.set_session_factory(session_factory)

    # Routes here
    config.add_route('welcome', '/')
    config.add_route('login', '/login')

    config.scan()
    return config.make_wsgi_app()


def authenticate(email, password):
    if email == '1' and password == '1':
        return 1
    else:
        return 0