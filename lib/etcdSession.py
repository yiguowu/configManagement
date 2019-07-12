class etcdSession:
    def __init__(self, connection=None):
        self.connection = connection

    def writeVersion(self, version):
        exclude = ["prefix"]
        print(version)

