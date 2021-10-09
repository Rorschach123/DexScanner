__author__ = 'Rorschach'

import logging
from Utils.HexUtil import *

DEX_HEADER_STRING_SIZE_VAL  = 0x38
DEX_HEADER_STRING_OFF_VAL   = 0x3C
DEX_HEADER_TYPE_SIZE_VAL    = 0x40
DEX_HEADER_TYPE_OFF_VAL     = 0x44
DEX_HEADER_PROTO_SIZE_VAL   = 0x48
DEX_HEADER_PROTO_OFF_VAL    = 0x4C
DEX_HEADER_FIELD_SIZE_VAL   = 0x50
DEX_HEADER_FIELD_OFF_VAL    = 0x54
DEX_HEADER_METHOD_SIZE_VAL  = 0x58
DEX_HEADER_METHOD_OFF_VAL   = 0x5C
DEX_HEADER_CLASS_SIZE_VAL   = 0x60
DEX_HEADER_CLASS_OFF_VAL    = 0x64
DEX_HEADER_DATA_SIZE_VAL    = 0x68
DEX_HEADER_DATA_OFF_VAL     = 0x6C

class DexAnalyzer:
    def __init__(self):
        pass

#DEX文件头解析
class DexHeaderProperty:
    stringIdxSize = 0
    stringIdxOff = 0
    typeIdxSize = 0
    typeIdxOff = 0
    methodIdsSize = 0
    methodIdsOff = 0
    classDefSize = 0
    classDefOff = 0

    def __init__(self,dexContent):
        # logging.info("--------------------Dex Header--------------------")
        self.classDefSize = self.readDexHeaderProperty(dexContent,DEX_HEADER_CLASS_SIZE_VAL,4)
        self.classDefOff = self.readDexHeaderProperty(dexContent,DEX_HEADER_CLASS_OFF_VAL,4)
        # logging.info("[Mess]read class def size and off is 0x%08X and 0x%08X", self.classDefSize,self.classDefOff)

        self.stringIdxSize = self.readDexHeaderProperty(dexContent,DEX_HEADER_STRING_SIZE_VAL,4)
        self.stringIdxOff = self.readDexHeaderProperty(dexContent,DEX_HEADER_STRING_OFF_VAL,4)
        # logging.info("[Mess]read string idx size and off is 0x%08X and 0x%08X", self.stringIdxSize,self.stringIdxOff)

        self.typeIdxSize = self.readDexHeaderProperty(dexContent,DEX_HEADER_TYPE_SIZE_VAL,4)
        self.typeIdxOff = self.readDexHeaderProperty(dexContent,DEX_HEADER_TYPE_OFF_VAL,4)
        # logging.info("[Mess]read type idx size and off is 0x%08X and 0x%08X", self.typeIdxSize,self.typeIdxOff)

        self.methodIdsSize = self.readDexHeaderProperty(dexContent,DEX_HEADER_METHOD_SIZE_VAL,4)
        self.methodIdsOff = self.readDexHeaderProperty(dexContent,DEX_HEADER_METHOD_OFF_VAL,4)
        # logging.info("[Mess]read method idx size and off is 0x%08X and 0x%08X", self.methodIdsSize,self.methodIdsOff)
        # logging.info("--------------------------------------------------")

    def verifyDex(self,dexContent):
        #魔术字校验
        isDex = True
        if self.readDexHeaderProperty(dexContent, 0x0, 8) != 0x003533300A786564:
            isDex = False

        return isDex

    def readDexHeaderProperty(self,dexContent,start,length):
        list1 = []
        for hexword in range(start,start+length):
            tmp = ord(dexContent[hexword])
            list1.append(tmp)

        number = endianToNormal(list1[0:length],length)
        return number

    def getClassNameByMethodNum(self, number, dexLoader):
        className = ""
        methodIdxOffset = number * 8 + self.methodIdsOff
        typeNum = endianToNormal(stringListToIntList(dexLoader.mapfile[methodIdxOffset + 0:methodIdxOffset + 2], 2), 2)
        classNameOffset = endianToNormal(stringListToIntList(dexLoader.mapfile[self.typeIdxOff + 4 * typeNum:self.typeIdxOff + 4 * typeNum + 2], 2), 2)
        classNameStrOffset = classNameOffset * 4 + self.stringIdxOff
        stringIdxImp = endianToNormal(stringListToIntList(dexLoader.mapfile[classNameStrOffset:classNameStrOffset + 4], 4), 4)
        stringlen = ord(dexLoader.mapfile[stringIdxImp])
        for strNum in range(0, stringlen):
            className += (dexLoader.mapfile[stringIdxImp + strNum + 1]).decode("gb2312")

        return className

    def getMethodNameByNumber(self, number, dexLoader):
        methodName = ""
        if number > self.methodIdsSize:
            return ""

        methodIdxOffset = number * 8 + self.methodIdsOff
        stringIdx = endianToNormal(stringListToIntList(dexLoader.mapfile[methodIdxOffset + 4:methodIdxOffset + 8], 4), 4) * 4 + self.stringIdxOff
        stringIdxImp = endianToNormal(stringListToIntList(dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
        stringlen = ord(dexLoader.mapfile[stringIdxImp])

        for strNum in range(0,stringlen):
            methodName += (dexLoader.mapfile[stringIdxImp+strNum+1]).decode("gb2312")

        return methodName

    def getStringByNumber(self, number, dexLoader):
        stringValue = ""
        if number > self.stringIdxSize:
            return ""

        stringIdx = number * 4 + self.stringIdxOff
        stringIdxImp = endianToNormal(stringListToIntList(dexLoader.mapfile[stringIdx:stringIdx+4],4),4)
        stringlen = ord(dexLoader.mapfile[stringIdxImp])
        for strNum in range(0, stringlen):
            try:
                stringValue += (dexLoader.mapfile[stringIdxImp + strNum + 1]).decode("gb2312")
            except:
                #TODO:判断非字符串编码就返回空，二进制检索会失效
                return ""

        return stringValue


#每个数据存储采用leb128数据类型存储
class DexClassDataHeader:
    staticFieldsSize = 0
    instanceFieldsSize = 0
    directMethodsSize = 0
    virtualMethodsSize = 0
    headerTakeBits = 0

    def __init__(self,dexContent,offset):
        analyStr = analyzeleb128(dexContent,offset + self.headerTakeBits)
        self.staticFieldsSize = analyStr[1]
        self.headerTakeBits += analyStr[0]
        analyStr = analyzeleb128(dexContent,offset + self.headerTakeBits)
        self.instanceFieldsSize = analyStr[1]
        self.headerTakeBits += analyStr[0]
        analyStr = analyzeleb128(dexContent,offset + self.headerTakeBits)
        self.directMethodsSize = analyStr[1]
        self.headerTakeBits += analyStr[0]
        analyStr = analyzeleb128(dexContent,offset + self.headerTakeBits)
        self.virtualMethodsSize = analyStr[1]
        self.headerTakeBits += analyStr[0]

class DexCode:
    className = ""
    methodName = ""
    methodType = ""
    registersSize = 0
    insSize = 0
    outsSize = 0
    triesSize = 0
    debugInfoOff = 0
    insnsSize = 0
    insns = []

    def __init__(self,offset,dexContent):
        self.registersSize = endianToNormal(stringListToIntList(dexContent[offset:offset+2],2),2)
        offset += 2
        self.insSize       = endianToNormal(stringListToIntList(dexContent[offset:offset+2],2),2)
        offset += 2
        self.outsSize      = endianToNormal(stringListToIntList(dexContent[offset:offset+2],2),2)
        offset += 2
        self.triesSize     = endianToNormal(stringListToIntList(dexContent[offset:offset+2],2),2)
        offset += 2
        self.debugInfoOff  = endianToNormal(stringListToIntList(dexContent[offset:offset+4],4),4)
        offset += 4
        self.insnsSize     = endianToNormal(stringListToIntList(dexContent[offset:offset+4],4),4)
        offset += 4
        insnsSize = self.insnsSize * 2
        self.insns = []

        while insnsSize != 0:
            insnsSize -= 1
            tmp = ord(dexContent[offset])
            offset += 1
            self.insns.append(tmp)

def analyzeleb128(dexContent,offset):
    listNumberAndValue = [1,0] # first means value take number of bits, second means value
    if ord(dexContent[offset]) > 0x7f:
        listNumberAndValue[0] += 1
        listNumberAndValue[1] = ord(dexContent[offset]) & 0x7f

        if ord(dexContent[offset+1]) > 0x7f:
            listNumberAndValue[0] += 1
            listNumberAndValue[1] = (listNumberAndValue[1] & 0x7f)|((ord(dexContent[offset+1]) & 0x7f)<<7)

            if ord(dexContent[offset+2]) > 0x7f:
                listNumberAndValue[0] += 1
                listNumberAndValue[1] |= ((ord(dexContent[offset+2]) & 0x7f)<<14)
                if ord(dexContent[offset+3]) > 0x7f:
                    listNumberAndValue[0] += 1
                    listNumberAndValue[1] |= ((ord(dexContent[offset+3]) & 0x7f)<<21)
                    listNumberAndValue[1] |= ((ord(dexContent[offset+4]) & 0x7f)<<28)
                else:
                    listNumberAndValue[1] |= ((ord(dexContent[offset+3]) & 0x7f)<<21)
            else:
                listNumberAndValue[1] |= ((ord(dexContent[offset+2]) & 0x7f)<<14)
        else:
            listNumberAndValue[1] = (listNumberAndValue[1] & 0x7f)|((ord(dexContent[offset+1]) & 0x7f)<<7)
    else:
        listNumberAndValue[1] = ord(dexContent[offset])
    return listNumberAndValue