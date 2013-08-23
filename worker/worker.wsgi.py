#!/usr/bin/python
import json
import plugins
import urlparse
import re
PATH_BASE = '/check/'


def application(environ, start_response):
    path = environ['PATH_INFO']
    query_string = environ['QUERY_STRING']
    query = urlparse.parse_qs(query_string)
    for (k, v) in query.items():
        query[k] = v[0]
    plugin_name = get_plugin_name(path)
    (status, result) = process(plugin_name, query)
    if status == '200 OK':
        response_headers = [('Content-Type', 'application/json')]
        response_body = json.dumps(result)

    else:
        response_headers = [('Content-Type', 'text/plain')]
        response_body = 'Error:%s' % result

    start_response(status, response_headers)
    return [response_body]


def get_plugin_name(path):
    result = re.match('^%s([^/]+)/?' % PATH_BASE, path)
    if result is not None:
        return result.group(1)
    else:
        return None


def process(plugin_name, args):
    # Try to get plugin class if exists
    try:
        plugin_class = getattr(plugins, plugin_name)
    except (AttributeError, TypeError) as e:
        return '404 Not Found', 'Invalid plugin name: %s' % plugin_name

    if plugin_class is not None:
        # Get plugin object
        try:
            plugin = plugin_class(**args)
        except Exception as e:
            return '500 Error', str("Can't create plugin object: %s\n" % e.message)

    # Getting result
    try:
        Result = plugin.check()
    except Exception as e:
        return 3, str("Can't get result from plugin: %s\n" % e.message)

    return '200 OK', Result