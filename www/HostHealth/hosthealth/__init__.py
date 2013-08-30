from pyramid.config import Configurator
from pyramid_beaker import BeakerSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Jinja templates here
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("hosthealth:templates")

    # Sessions here
    config.include("pyramid_beaker")
    session_factory = BeakerSessionFactoryConfig(
        type='file',
        key='session_id',
        secret='Please Keep 1t Encrypted',
        data_dir='/tmp/hh/sessions/data',
        data_lock_dir='/tmp/hh/sessions/lock',
        timeout=3600,  # 1 hour sessions
    )
    config.set_session_factory(session_factory)

    # Routes here
    config.add_route('dashboard', '/dashboard')
    config.add_route('welcome', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('hosts', '/hosts')

    config.scan()
    return config.make_wsgi_app()
