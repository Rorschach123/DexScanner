__author__ = 'Rorschach'
import logging

class DexMap:
    fileSize = 0
    basePointer = []
    className = ""

    def __init__(self):
        self.className = "Dex map"
        self.fileSize = 0
        self.basePointer = []

    def SetPointer(self,basePointer):
        self.basePointer = basePointer

    def GetPointer(self):
        return self.basePointer

    def GetFileSize(self):
        return self.fileSize

    def ReadFile(self,path):
        fileObj = open(path,'rb')
        fileObj.seek(0,2)
        self.fileSize = fileObj.tell()
        fileObj.seek(0,0)
        basePointer = []

        try:
            for num in range(0,self.fileSize):
                ch = fileObj.read(1)
                basePointer.append(ch)
#               basePointer.append(int(hex(ord(ch)).replace('0x', ''),16))
        finally:
            fileObj.close()
        if basePointer == []:
            return False
        self.SetPointer(basePointer)
        return True