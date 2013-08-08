# tcp plugin for hh
from base import plugin_base
from args import address


class plugin(plugin_base):
    use_args = [address]
    description = "Simple TCP plugin for HH"



