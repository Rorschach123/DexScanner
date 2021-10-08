__author__ = 'Rorschach'

from DexHandler import DexFormAnalyzer
from DetectRules.Rules import *
from DetectRules.SmaliMarco import *
import logging

class Detecter:
    dexLoader = None

    def __init__(self):
        self.dexLoader = None

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

                # TODO:NOP之后跟着SWITCH-CASE的情况
                if opcode == 0x0:
                    calcuCodeLen = codeLen
                    break

                self.detectOpcode(opcode, ins[calcuCodeLen:], rules, dexHeader, className, methodName)

                calcuCodeLen += opcodeLen

            if calcuCodeLen != codeLen:
                logging.error(className + "_" + methodName)
                break

    #opcode判断是否覆盖在规则内
    def detectOpcode(self, opcode, ins, rules, dexHeader, currentClass, currentMethod):
        for rule in rules:
            if rule.type == FIND_CALL_STATIC_METHOD:
                if opcode == INS_INVOKE_STATIC:
                    if self.detectStaticMethod(ins, rule, dexHeader) == 1:
                        logging.info("[%s][%s] ----- [%s][%s]" %(rule.className,  rule.methodName, currentClass, currentMethod))
            elif rule.type == FIND_CALL_DIRECT_METHOD:
                if opcode == INS_INVOKE_DIRECT:
                    if self.detectDirectMethod(ins, rule, dexHeader) == 1:
                        logging.info("[%s][%s] ----- [%s][%s]" %(rule.className,  rule.methodName, currentClass, currentMethod))
            elif rule.type == FIND_CALL_VIRTUAL_METHOD:
                if opcode == INS_INVOKE_VIRTUAL:
                    if self.detectVirtualMethod(ins, rule, dexHeader) == 1:
                        logging.info("[%s][%s] ----- [%s][%s]" %(rule.className,  rule.methodName, currentClass, currentMethod))
            elif rule.type == FIND_CALL_SUPER_METHOD:
                #TODO
                pass
            elif rule.type == FIND_PUT_STRING:
                #TODO
                pass
            elif rule.type == FIND_PUT_VALUE:
                #TODO
                pass

    #static方法检索
    def detectStaticMethod(self, ins, rule, dexHeader):
        methodNum = (ins[2] & 0xff) | ((ins[3] << 8) & 0xff00)
        methodName = dexHeader.getMethodNameByMethodNum(methodNum, self.dexLoader)
        if methodName != rule.methodName:
            return 0

        className = dexHeader.getClassNameByMethodNum(methodNum, self.dexLoader)
        if className == rule.className:
            return 1
        else:
            return 0

    #virtual方法检索
    def detectVirtualMethod(self, ins, rule, dexHeader):
        methodNum = (ins[2] & 0xff) | ((ins[3]  << 8) & 0xff00)
        methodName = dexHeader.getMethodNameByMethodNum(methodNum, self.dexLoader)

        if methodName == rule.methodName:
            return 1
        else:
            return 0

    #direct方法检索
    def detectDirectMethod(self, ins, rule, dexHeader):
        methodNum = (ins[2] & 0xff) | ((ins[3] << 8) & 0xff00)
        methodName = dexHeader.getMethodNameByMethodNum(methodNum, self.dexLoader)
        if methodName != rule.methodName:
            return 0

        className = dexHeader.getClassNameByMethodNum(methodNum, self.dexLoader)
        if className == rule.className:
            return 1
        else:
            return 0




