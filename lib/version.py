import inspect
from lib.parameter import parameter

class version:
    def __init__(self, version, parent=None, desc=None, freeze=False, driver=None):
        self.version = version
        self.desc = desc
        self.freeze = freeze
        self.driver = driver
        self.parent = parent
        self.prefix = "paramter/"+self.version+"/"
        self.parameterList = []

    def addParameter(self, param):
        for i in self.parameterList:
            if i.getKey() == param.getKey():
                return False
        self.parameterList.append(param)
        return True
    
    def frozen(self):
        self.freeze = True

    def validateDriver(self, drv):
        check = ["connection"]
        for name, data in inspect.getmembers(drv):
            if name in check:
                attr = getattr(drv, name)
                if attr is not None:
                    check.remove(name)
        if len(check) > 0:
            return False
        return True

    def setDriver(self, drv):
        if self.validateDriver(drv):
            self.driver = drv