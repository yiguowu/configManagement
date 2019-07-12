import time

class parameter:
    def __init__(self, key, status="active", state="dirty",value=None, lastChange = None, timestamp = None, type="static", owner = None):
        self.key = key
        self.value = value
        self.status = status
        self.state = state
        self.lastChange = lastChange
        self.type = type
        self.owner = owner
        if timestamp is None:
            self.timestamp = int(time.time())
        else:
            self.timestamp = timestamp

    def generateAPI(self):
        item = {}
        item["_metadata"] = {}
        item["_metadata"]["state"] = self.state
        item["_metadata"]["owner"] = self.owner
        item["_metadata"]["lastChange"] = self.lastChange
        item["_metadata"]["status"] = self.status
        item["_metadata"]["type"] = self.type
        item["_metadata"]["owner"] = self.owner
        item["_metadata"]["timestamp"] = self.timestamp
        item["value"] = self.value
        return self.key, item

    def setStatus(self, status, lastChange=None, owner = None):
        self.status = status
        self.state = "dirty"
        self.owner = owner
        self.timestamp = int(time.time())
        self.lastChange = lastChange

    def getState(self):
        return self.state

    def getStatus(self):
        return self.status

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def updateValue(self, value, lastChange=None, owner=None):
        self.value = value
        self.state = "dirty"
        self.lastChange = lastChange
        self.owner = owner
        self.timestamp = int(time.time())