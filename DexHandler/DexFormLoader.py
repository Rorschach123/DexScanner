__author__ = 'Rorschach'

from DexHandler import DexFormAnalyzer
from Utils.HexUtil import *
import logging

DEX_CLASS_DEF_ITEM_CLASS_DATA_OFF_VAL = 0x18
DEX_CLASS_DEF_ITEM_SIZE = 0x20

class DexLoader:
    mapfile = []
    dexMethodCodes = []

    def __init__(self):
        self.mapfile = []
        self.dexMethodCodes = []
        self.dexClassName = []
        self.dexMethodName = []

    def getMapFile(self, mapFile, dexPath):
        if mapFile.readFile(dexPath):
            self.mapfile = mapFile.getPointer()

    def jumpToNextField(self,dexContent,classDataOffset,size,times):
        for i in range(0,size*times):
            listNumberAndValue = DexFormAnalyzer.analyzeleb128(dexContent, classDataOffset)
            classDataOffset += listNumberAndValue[0]
        return classDataOffset

    #解析加载所有类和方法
    def loadAllClassAndMethod(self, dexHeader):
        #DexClassDef Obj(classIdx) -> DexClassData(DexClassDataHeader & directMethods & virtualMethods) -> DexClassDataHeader(2 type of method size) -> DexMethod(methodIdx & codeOff) -> DexMethodId(nameIdx) -> Get Method Name
        #                                                                                                                                                                              -> DexCode -> Get method message & ins

        #读取类定义的数据段大小和偏移
        classDefSize = dexHeader.classDefSize
        classDefOff = dexHeader.classDefOff

        for i in range(0,classDefSize):
            offset = classDefOff + i * DEX_CLASS_DEF_ITEM_SIZE

            #获取类名
            strClassName = ""
            classDefClassIdx = DexFormAnalyzer.endianToNormal(stringListToIntList(self.mapfile[offset:offset + 4], 4), 4)
            typeOffset = classDefClassIdx * 4 + dexHeader.typeIdxOff
            classDefItemStringIdx = DexFormAnalyzer.endianToNormal(stringListToIntList(self.mapfile[typeOffset:typeOffset + 4], 4), 4)
            stringOffset = 4 * classDefItemStringIdx + dexHeader.stringIdxOff
            stringDataOff = DexFormAnalyzer.endianToNormal(stringListToIntList(self.mapfile[stringOffset:stringOffset + 4], 4), 4)
            strLen = ord(self.mapfile[stringDataOff])
            for j in range(0,strLen):
                strClassName += (self.mapfile[stringDataOff + 1 + j]).decode("gb2312")
            # logging.info("[ClassName]" + strClassName)

            #类类型是android.support.*类型,忽略
            if strClassName.startswith("Landroid/support/"):
                continue

            #继续解析类预定义结构体#
            #获取类的数据,先找对应类数据在文件中的偏移位置
            offset += DEX_CLASS_DEF_ITEM_CLASS_DATA_OFF_VAL
            data = []
            for value in self.mapfile[offset:offset+4]:
                data.append(ord(value))
            classDataItem = DexFormAnalyzer.endianToNormal(data, 4)
            if classDataItem == 0x0:
                continue
            #解析类中数据,得到各种变量方法数量的统计
            dexClassDataHeader = DexFormAnalyzer.DexClassDataHeader(self.mapfile, classDataItem)
            #统计数量不是定长的变量,因此加上偏移才是类数据的内容
            classDataItemPointer = classDataItem + dexClassDataHeader.headerTakeBits

            #跳过变量字段的定义
            classDataItemPointer = self.jumpToNextField(self.mapfile,classDataItemPointer,dexClassDataHeader.staticFieldsSize,2)        #DexField has 2 fields
            classDataItemPointer = self.jumpToNextField(self.mapfile,classDataItemPointer,dexClassDataHeader.instanceFieldsSize,2)
            classDataOffset = classDataItemPointer
            #开始对方法进行解析
            classDataOffset = self.loadMethod(classDataOffset, dexClassDataHeader.directMethodsSize, dexHeader, "Direct", strClassName)
            self.loadMethod(classDataOffset, dexClassDataHeader.virtualMethodsSize, dexHeader, "Virual", strClassName)

    #加载所有方法
    def loadMethod(self, classDataOffset, methodsSize, dexHeader, methodType, strClassName):
        listNumberAndValueBase = 0
        for methodNum in range(0,methodsSize * 3):
            listNumberAndValue = DexFormAnalyzer.analyzeleb128(self.mapfile, classDataOffset)
            classDataOffset += listNumberAndValue[0]

            if methodNum % 3 == 0:
                if methodNum == 0:
                    listNumberAndValueBase = listNumberAndValue[1]
                else:
                    listNumberAndValue[1] += listNumberAndValueBase
                    listNumberAndValueBase = listNumberAndValue[1]

                #DexMethod(methodIdx & codeOff)
                methodIdxImp = listNumberAndValue[1] * 8 + dexHeader.methodIdsOff
                methodIdxImp += 4
                if methodIdxImp > len(self.mapfile):
                    break
                stringIdx = DexFormAnalyzer.endianToNormal(
                    DexFormAnalyzer.stringListToIntList(self.mapfile[methodIdxImp:methodIdxImp + 4], 4), 4) * 4 + dexHeader.stringIdxOff
                stringIdxImp = DexFormAnalyzer.endianToNormal(
                    DexFormAnalyzer.stringListToIntList(self.mapfile[stringIdx:stringIdx + 4], 4), 4)
                stringlen = ord(self.mapfile[stringIdxImp])
                strMethodName = ""
                for strNum in range(0,stringlen):
                    strMethodName += (self.mapfile[stringIdxImp+strNum+1]).decode("gb2312")
              #  print "--DbIF-- " + methodType +" Method: " + str

            #analyze dex method code
            if (methodNum+1) % 3 == 0:
                if listNumberAndValue[1] != 0:
                    self.getMethodCode(listNumberAndValue[1], strClassName, strMethodName, methodType)

        return classDataOffset

    #获取方法的字节码
    def getMethodCode(self, offset, className, methodName, methodType):
        dexCode = DexFormAnalyzer.DexCode(offset, self.mapfile)
        dexCode.className = className
        dexCode.methodName = methodName
        dexCode.methodType = methodType
        # if dexCode.methodName == "onCreate":
        #     logging.info("[MethodName]" + dexCode.methodName + "[Code]" + ",".join([hex(_) for _ in dexCode.insns]))

        self.dexMethodCodes.append(dexCode)

