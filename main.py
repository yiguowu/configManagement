from lib.etcdConnection import etcdConnection
from lib.etcdSession import etcdSession
from lib.version import version

if __name__ == "__main__":
    cnt = etcdConnection()
    session = etcdSession(connection=cnt)
    version = version("1.3")
    version.setDriver(session)
    session.writeVersion(version.generateAPL())
    session.listVersion()