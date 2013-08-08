class plugin_base():
    """ Base class for HH plugins"""
    description = 'HH plugin'
    use_args = {}  # args classes to use
    args = {}

    def __init__(self, **dirty_args):
        self.dirty_args = dirty_args
        self.make_args()

    def make_args(self):
        for arg_class in self.use_args:
            arg = arg_class()
            if (not arg.name in self.dirty_args) and arg.mandatory:
                # TODO: We must handle it!
                raise PluginArgumentValidation('Mandatory argument \'%s\' missed' % (arg.name,))
            self.args[arg.name] = arg.validate(self.dirty_args[arg.name])


class PluginArgumentValidation(Exception):
    pass