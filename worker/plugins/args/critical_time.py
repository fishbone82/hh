# critical_time argument for HH plugins
from worker.plugins.args.base import plugin_arg


class arg(plugin_arg):
    name = 'critical_time'
    mandatory = 0
    default_value = 0.5
    force_default = 1