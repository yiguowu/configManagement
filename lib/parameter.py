class parameter:
    def __init__(self, key, value=None, version= None, session=None):
        self.key = key
        self.value = value
        self.version = version
        self.session = session

    def getValue(self):
        return self.value

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def updateValue(self, value, version):
        self.value = value
        self.version = version



