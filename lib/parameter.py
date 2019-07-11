class parameter:
    def __init__(self, key, status="active", type="string",value=None):
        self.key = key
        self.value = value
        self.type = type
        self.status = status

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status
    
    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def updateValue(self, value):
        self.value = value