# port argument for HH plugins
from base import plugin_arg


class arg(plugin_arg):
    name = 'port'
    mandatory = 1

    def validate(self, dirty_value):
        return int(dirty_value)