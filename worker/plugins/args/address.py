# address argument for HH plugins
from worker.plugins.args.base import plugin_arg


class arg(plugin_arg):
    name = 'address'
    mandatory = 1