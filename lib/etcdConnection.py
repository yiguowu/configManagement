import etcd3
class etcdConnection:
    def __init__(self, address="127.0.0.1", port=2379):
        self.connection = etcd3.client(host=address, port=port)

    def getConnection(self):
        return self.connection

    def closeConnection(self):
        self.connection.close()
