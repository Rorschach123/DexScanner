
NOT_SET             = -1
FIND_CALL_STATIC_METHOD     = 0x01
FIND_CALL_DIRECT_METHOD     = 0x02
FIND_CALL_SUPER_METHOD      = 0x03
FIND_CALL_VIRTUAL_METHOD    = 0x04
FIND_PUT_STRING             = 0x05
FIND_PUT_VALUE              = 0x06

class Rules:
    type = NOT_SET
    methodName = ""
    className = ""

    #方法调用查找
    #字符串查找
    #数值查找
    def __init__(self, type, methodName="", className=""):
        self.type = type
        self.methodName = methodName
        self.className = className
        pass
