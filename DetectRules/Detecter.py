__author__ = 'Rorschach'

from DexHandler import DexFormAnalyzer
from DetectRules.Rules import *
from DetectRules.SmaliMarco import *
import logging

class Detecter:
    className = ""
    dexLoader = None

    def __init__(self):
        self.className = "Detecter"
        self.dexLoader = None

    def checkingInsAndTypeValue(self,insNum,ins,dexHeader,insValue,strDes):
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

    def checkingInsAndClassValue(self,insNum,ins,dexHeader,insValue,methodName,className):
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

    def checkingInsAndMethodValue(self,insNum,ins,dexHeader,insValue,strDes):
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

    def checkingInsAndIncludeStrValue(self,insNum,ins,dexHeader,insValue,strDes):
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

    def checkingInsAndStrValue(self,insNum,ins,dexHeader,insValue,strDes):
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

    def detectOpcode(self, opcode, opcodeLen, ins, rules):
        for rule in rules:
            if rule.type == FIND_CALL_STATIC_METHOD:
                pass
            elif rule.type == FIND_CALL_DIRECT_METHOD:
                if opcode == INS_INVOKE_DIRECT:
                    pass
            elif rule.type == FIND_CALL_SUPER_METHOD:
                pass
            elif rule.type == FIND_CALL_VIRTUAL_METHOD:
                pass
            elif rule.type == FIND_PUT_STRING:
                pass
            elif rule.type == FIND_PUT_VALUE:
                pass

    #扫描smali捕捉API
    def detectApkApi(self, dexFormLoader, dexHeader, rules):
        self.dexLoader = dexFormLoader

        for codeNum in range(0,len(self.dexLoader.dexMethodCodes)):
            ins = self.dexLoader.dexMethodCodes[codeNum].insns
            className = self.dexLoader.dexMethodCodes[codeNum].className
            methodName = self.dexLoader.dexMethodCodes[codeNum].methodName

            codeLen = len(ins)
            calcuCodeLen = 0
            while codeLen > calcuCodeLen:
                opcode = ins[calcuCodeLen]                  #获取当前指令opcode
                opcodeLen = SMALI_OPCODE_DEF[opcode][1]     #指令对应长度解析
                calcuCodeLen += opcodeLen

                # TODO:NOP之后跟着SWITCH-CASE的情况
                if opcode == 0x0:
                    calcuCodeLen = codeLen
                    break

                self.detectOpcode(opcode, opcodeLen, ins[calcuCodeLen:], rules)

            if calcuCodeLen != codeLen:
                # logging.error("Code len calculate error : " + ",".join(hex(_) for _ in ins))
                # logging.error("%d : %d" %(codeLen, calcuCodeLen))
                logging.error(className + "_" + methodName)

                # calcuCodeLen = 0
                # while codeLen > calcuCodeLen:
                #     opcode = ins[calcuCodeLen]
                #     opcodeLen = SMALI_OPCODE_DEF[opcode][1]
                #     calcuCodeLen += opcodeLen
                #     logging.error("%x" %opcode)
                break


            # for insNum in range(0,len(ins) - 2):
            #     for rule in rules:
            #         if rule.checkType == CHECK_CLASS_TYPE:
            #             if self.checkingInsAndClassValue(insNum, ins, dexHeader, rule.insValue, rule.methodName, rule.className) != 0:
            #                 logging.info("[Detect]" + rule.className + "_" + rule.methodName + "[Class]" + className + "[Method]" + methodName)
            #         elif rule.checkType == CHECK_METHOD_TYPE:
            #             if self.checkingInsAndMethodValue(insNum, ins, dexHeader,rule.insValue, rule.methodName) != 0:
            #                 logging.info("[Detect]" + rule.methodName + "[Class]" + className + "[Method]" + methodName)
                    # elif rule.checkType == CHECK_TYPE_TYPE:
                    #     result = self.checkingInsAndClassValue(insNum, ins, dexHeader,rule.insValue, rule.methodName, rule.className)
                    # elif rule.checkType == CHECK_TYPE_FIELD:
                    #     result = self.checkingInsAndClassValue(insNum, ins, dexHeader,rule.insValue, rule.methodName, rule.className)

                        # if resultDexClassLoader[0] > 0 and resultDexClassLoader[1] > 0:
                        #     countFindDexClassLoader += 1
                        #     logging.info("[Detc]DexClassLoader : ClassName = " + self.dexLoader.dexClassName[
                        #         codeNum] + " MethodName = " + self.dexLoader.dexMethodName[codeNum])
                        # else:
                        #     if resultDexClassLoader[0] > 0:
                        #         countFindDexClassLoaderPossible += 1
                        #         logging.info(
                        #             "[Detc]Possible_DexClassLoader : ClassName = " + self.dexLoader.dexClassName[
                        #                 codeNum] + " MethodName = " + self.dexLoader.dexMethodName[codeNum])





