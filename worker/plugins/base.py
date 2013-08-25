class plugin_base():
    """ Base class for Orthus plugins"""
    description = 'Orthus plugin'
    use_args = {}  # args classes to use
    args = {}
    status = -1
    data = None

    def __init__(self, **dirty_args):
        self.dirty_args = dirty_args
        self.make_args()

    def make_args(self):
        for arg_class in self.use_args:
            arg = arg_class()
            if not arg.name in self.dirty_args:
                if arg.mandatory:
                    # TODO: We must handle it somewhere!
                    raise PluginArgumentValidation('Mandatory argument \'%s\' missed' % (arg.name,))
                else:
                    self.args[arg.name] = arg.default_value
            else:
                self.args[arg.name] = arg.validate(self.dirty_args[arg.name])

    def check(self):
        self.process()
        return self.status, self.data

    def process(self):
        pass


class PluginArgumentValidation(Exception):
    pass