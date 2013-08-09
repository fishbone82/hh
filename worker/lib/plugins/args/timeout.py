# timeout argument for HH plugins
from base import plugin_arg


class arg(plugin_arg):
    name = 'timeout'
    mandatory = 0
    default_value = 3
    force_default = 1