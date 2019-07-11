from lib.etcdConnection import etcdConnection
from lib.etcdSession import etcdSession
from lib.versison import version

if __name__ == "__main__":
    cnt = etcdConnection()
    session = etcdSession(connection=cnt)
    version = version("1.0")
    version.setDriver(session)