class parameter:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def getValue(self):
        return self.value

    def updateValue(self, value, version):
        self.value = value