# warning_time argument for Orthus plugins
from base import plugin_arg


class arg(plugin_arg):
    name = 'warning_time'
    mandatory = 0
    default_value = 0.3
    force_default = 1