class version:
    def __init__(self, version, desc=None, freeze=False):
        self.version = version
        self.desc = desc
        self.freeze = freeze

    def frozen(self):
        self.freeze = True

    