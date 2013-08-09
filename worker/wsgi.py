import sys
import json
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

sys.path.append('lib')
import plugins


def worker(req):
    resp = Response(content_type='application/json', charset='utf8')
    (err, result) = process(req)
    if err:
        resp.content_type = 'text/html'
        resp.app_iter = str(err)
    else:
        resp.app_iter = json.dumps(result)
    return resp


def process(req):
    error = None

    # Trying to get plugin class if exists
    try:
        plugin_class = getattr(plugins, req.matchdict['plugin_name'])
    except AttributeError:
        return str("Invalid plugin name: %s\n" % req.matchdict['plugin_name']), None

    # Getting plugin object
    try:
        plugin = plugin_class(**req.params.mixed())
    except Exception as e:
        return str("Can't create plugin object: %s\n" % e.message), None

    # Getting result
    try:
        result = plugin.check()
    except Exception as e:
        return str("Can't get result from plugin: %s\n" % e.message), None

    return error, result

if __name__ == '__main__':
    config = Configurator()
    config.add_route('worker', '/check/{plugin_name}')
    config.add_view(worker, route_name='worker')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()