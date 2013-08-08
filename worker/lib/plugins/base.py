class plugin_base():
    """ Base class for HH plugins"""
    description = 'HH plugin'
    use_args = None  # args classes to use

    def __init__(self, **dirty_args):
        self.dirty_args = dirty_args
        self.make_args()

    def make_args(self):
        pass

