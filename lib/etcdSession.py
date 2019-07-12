class etcdSession:
    def __init__(self, connection=None):
        self.connection = connection.getConnection()

    def writeVersion(self, APL):
        exclude = ["prefix"]
        prefix = APL["_metadata"]["prefix"]
        for item in APL:
            for entry in APL[item]:
                key = prefix + item + "/" + entry
                if entry not in exclude:
                    value = str(APL[item][entry])
                    self.connection.put(key,value)

    def listVersion(self):
        val = self.connection.get_prefix("parameter")
        print(val)
        for i, j in val:
            print(i,j.key)

    def readVersion(self):
        val = self.connection.get("parameter/1.1/_metadata/version")
        print(val)



