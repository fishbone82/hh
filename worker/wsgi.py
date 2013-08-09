import sys
import json
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

sys.path.append('lib')
import plugins


def worker(req):
    resp = Response(content_type='application/json', charset='utf8')
    try:
        plugin_class = getattr(plugins, req.matchdict['plugin_name'])
    except AttributeError:
        return Response('Invalid plugin name: %s' % req.matchdict['plugin_name'])

    plugin = plugin_class(**req.params.mixed())
    result = plugin.check()

    resp.app_iter = json.dumps(result)
    return resp

if __name__ == '__main__':
    config = Configurator()
    config.add_route('worker', '/check/{plugin_name}')
    config.add_view(worker, route_name='worker')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()