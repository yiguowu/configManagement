class etcdSession:
    def __init__(self, connection=None):
        self.connection = connection.getConnection()

    def writeVersion(self, version):
        exclude = ["prefix"]
        prefix = version["_metadata"]["prefix"]
        for item in version:
            for entry in version[item]:
                key = prefix + item + "/" + entry
                if entry not in exclude:
                    value = str(version[item][entry])
                    self.connection.put(key,value)
                    print(key,value)

    def readVersion(self):
        val = self.connection.get("paramter/1.0/_metadata/version")
        print(val)



