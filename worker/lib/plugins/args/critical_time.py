# critical_time argument for HH plugins
from base import plugin_arg


class arg(plugin_arg):
    name = 'critical_time'
    mandatory = 0
    default_value = 2
    force_default = 1