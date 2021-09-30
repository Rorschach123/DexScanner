
NOT_SET             = -1
CHECK_CLASS_TYPE    = 1
CHECK_METHOD_TYPE   = 2
CHECK_TYPE_TYPE     = 3
CHECK_TYPE_FIELD    = 4

class Rules:
    checkType = NOT_SET
    insValue = NOT_SET
    typeName = ""
    methodName = ""
    className = ""

    def __init__(self, insValue, checkType, typeName="", methodName="", className=""):
        self.checkType = checkType
        self.insValue = insValue
        self.typeName = typeName
        self.methodName = methodName
        self.className = className
        pass
