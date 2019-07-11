class parameter:
    def __init__(self, key, status="active", state="dirty",value=None):
        self.key = key
        self.value = value
        self.status = status
        self.state = state

    def setStatus(self, status):
        self.status = status

    def getState(self):
        return self.state

    def getStatus(self):
        return self.status

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def updateValue(self, value):
        self.value = value
        self.state = "dirty"