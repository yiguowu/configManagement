from lib.etcdConnection import etcdConnection
from lib.etcdSession import etcdSession

if __name__ == "__init__":
    cnt = etcdConnection()
    session = etcdSession(connection=cnt)
