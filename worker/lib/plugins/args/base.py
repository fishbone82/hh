# Base class for HH plugins arguments


class plugin_arg():
    name = None
    default_value = None
    mandatory = 0       # by default args is not mandatory
    force_default = 0   # replace value by default if validation failed

    def validate(self, dirty_value):
        return dirty_value # TODO: we must validate it somehow!