import etcd3

class etcdSession:
    def __init__(self, connection=None):
        self.connection = connection