# Base class for HH plugins arguments


class plugin_arg():
    name = None
    default = None
    force_default = 0  # replace value by default if validation failed
    value = None

    def __init__(self):
        pass

    def validate(self):
        pass