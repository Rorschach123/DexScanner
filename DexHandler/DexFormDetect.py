__author__ = 'Rorschach'

from DexHandler import DexFormAnalyzer
import logging

class DexDetect:
    className = ""
    dexLoader = None

    def __init__(self):
        self.className = "Dex Detect"
        self.dexLoader = None

    def SetDexLoaderObj(self,dexLoader):
        self.dexLoader = dexLoader

    def CheckingInsAndTypeValue(self,insNum,ins,dexHeader,insValue,strDes):
        str = ""
        if insNum % 2 == 0 and ins[insNum] == insValue:
        #      print self.dexLoader.dexClassName[codeNum] + "--" + self.dexLoader.dexMethodName[codeNum]
            typeNum = (ins[insNum+2] & 0xff) | ((ins[insNum+3]  << 8) & 0xff00)
            if typeNum > dexHeader.typeIdxSize:
                return 0
            typeIdxOffset = typeNum * 4 + dexHeader.typeIdxOff
            stringIdx = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[typeIdxOffset:typeIdxOffset + 4], 4), 4) * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                str += self.dexLoader.mapfile[stringIdxImp+strNum+1]

        if str == strDes:
            return 1
        else:
            return 0

    def CheckingInsAndClassValue(self,insNum,ins,dexHeader,insValue,methodName,className):
        str = ""
        classStr = ""
        if insNum % 2 == 0 and ins[insNum] == insValue:
            methodNum = (ins[insNum+2] & 0xff) | ((ins[insNum+3]  << 8) & 0xff00)
            if methodNum > dexHeader.methodIdsSize:
                return 0
            methodIdxOffset = methodNum * 8 + dexHeader.methodIdsOff
            stringIdx = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[methodIdxOffset + 4:methodIdxOffset + 8], 4), 4) * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
            # if stringIdxImp > len(self.dexLoader.mapfile):
            #     return 0
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                str += (self.dexLoader.mapfile[stringIdxImp+strNum+1]).decode("gb2312")

            if str != methodName:
                return 0
            #type idx
            classStr = ""
            typeNum = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[methodIdxOffset + 0:methodIdxOffset + 2], 2), 2)
            classNameOffset =  DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[dexHeader.typeIdxOff + 4 * typeNum:dexHeader.typeIdxOff + 4 * typeNum + 2], 2), 2)
            classNameStrOffset = classNameOffset * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[classNameStrOffset:classNameStrOffset + 4], 4), 4)
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                classStr += (self.dexLoader.mapfile[stringIdxImp+strNum+1]).decode("gb2312")
        if classStr == className:
            return 1
        else:
            return 0


    def CheckingInsAndMethodValue(self,insNum,ins,dexHeader,insValue,strDes):
        str = ""
        if insNum % 2 == 0 and ins[insNum] == insValue:
            methodNum = (ins[insNum+2] & 0xff) | ((ins[insNum+3]  << 8) & 0xff00)
            if methodNum > dexHeader.methodIdsSize:
                return 0
            methodIdxOffset = methodNum * 8 + dexHeader.methodIdsOff
            stringIdx = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[methodIdxOffset + 4:methodIdxOffset + 8], 4), 4) * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
            # if stringIdxImp > len(self.dexLoader.mapfile):
            #     return 0
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                str += (self.dexLoader.mapfile[stringIdxImp+strNum+1]).decode("gb2312")

        if str == strDes:
            return 1
        else:
            return 0

    def CheckingInsAndIncludeStrValue(self,insNum,ins,dexHeader,insValue,strDes):
        str = ""
        if insNum % 2 == 0 and ins[insNum] == insValue:
        #      print self.dexLoader.dexClassName[codeNum] + "--" + self.dexLoader.dexMethodName[codeNum]
            strNum = (ins[insNum+2] & 0xff) | ((ins[insNum+3]  << 8) & 0xff00)
            if strNum > dexHeader.stringIdxSize:
                return 0
            stringIdx = strNum * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                str += self.dexLoader.mapfile[stringIdxImp+strNum+1]

        if strDes in str:
            return 1
        else:
            return 0

    def CheckingInsAndStrValue(self,insNum,ins,dexHeader,insValue,strDes):
        str = ""
        if insNum % 2 == 0 and ins[insNum] == insValue:
        #      print self.dexLoader.dexClassName[codeNum] + "--" + self.dexLoader.dexMethodName[codeNum]
            strNum = (ins[insNum+2] & 0xff) | ((ins[insNum+3]  << 8) & 0xff00)
            if strNum > dexHeader.stringIdxSize:
                return 0
            stringIdx = strNum * 4 + dexHeader.stringIdxOff
            stringIdxImp = DexFormAnalyzer.endianToNormal(
                DexFormAnalyzer.stringListToIntList(self.dexLoader.mapfile[stringIdx:stringIdx + 4], 4), 4)
            stringlen = ord(self.dexLoader.mapfile[stringIdxImp])
            for strNum in range(0,stringlen):
                str += self.dexLoader.mapfile[stringIdxImp+strNum+1]

        if str == strDes:
            return 1
        else:
            return 0

    def DetectApkApi(self,dexHeader):
        #Loop All method code to check
        logging.info("[Detc]Start Checking if has Some Api")
        countFindDexClassLoader = 0
        countFindDexClassLoaderPossible = 0

        for codeNum in range(0,len(self.dexLoader.dexMethodCodes)):
            ins = self.dexLoader.dexMethodCodes[codeNum].insns
            resultDexClassLoader = [0,0]

            for insNum in range(0,len(ins) - 2):
                resultDexClassLoader = self.DetectDexClassLoader(dexHeader,insNum,ins,resultDexClassLoader)

            if resultDexClassLoader[0] > 0 and resultDexClassLoader[1] > 0:
                countFindDexClassLoader += 1
                logging.info("[Detc]DexClassLoader : ClassName = " + self.dexLoader.dexClassName[codeNum] + " MethodName = " + self.dexLoader.dexMethodName[codeNum])
            else:
                if resultDexClassLoader[0] > 0:
                    countFindDexClassLoaderPossible += 1
                    logging.info("[Detc]Possible_DexClassLoader : ClassName = " + self.dexLoader.dexClassName[codeNum] + " MethodName = " + self.dexLoader.dexMethodName[codeNum])

        if countFindDexClassLoader != 0:
            logging.info("[Detc]Find DexClassLoader Api,Count number = %d", countFindDexClassLoader)
        else:
            logging.info("[Detc]Not Found DexClassLoader Api")
        if countFindDexClassLoaderPossible != 0:
            logging.info("[Detc]Find Possible DexClassLoader Api,Count number = %d", countFindDexClassLoaderPossible)


    def DetectDexClassLoader(self,dexHeader,insNum,ins,resultDexClassLoader):
        #init dexclassloader
        #loadClass
        resultDexClassLoader[0] += self.CheckingInsAndClassValue(insNum,ins,dexHeader,0x70,"<init>","Ldalvik/system/DexClassLoader;")
        resultDexClassLoader[1] += self.CheckingInsAndMethodValue(insNum,ins,dexHeader,0x6E,"loadClass")
        return resultDexClassLoader