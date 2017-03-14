__author__ = 'Rorschach'

import DexFormAnalyzer

class DexLoader:
    mapfile = []
    dexMethodCodes = []
    dexClassName = []
    dexMethodName = []
    className = ""

    def __init__(self):
        self.className = "Dex Loader"
        self.mapfile = []
        self.dexMethodCodes = []
        self.dexClassName = []
        self.dexMethodName = []

    def GetMapFile(self,mapFile,dexPath):
        if mapFile.ReadFile(dexPath):
            print "--Load-- Read Dex File Success"
        self.mapfile = mapFile.GetPointer()

    def jumpToNextField(self,dexContent,classDataOffset,size,times):
        for i in range(0,size*times):
            listNumberAndValue = DexFormAnalyzer.analyzeleb128(dexContent,classDataOffset)
            classDataOffset += listNumberAndValue[0]
        return classDataOffset

    def LoadAllClassAndMethod(self,dexHeader):
        #Traversal all class.method,query order:
        #DexHeader(classDefsSize & classDefsOff) -> DexClassDef(classIdx) -> DexTypeId(descriptorIdx) -> DexStringId(stringDataOff) ->Get Class Name
        #DexClassDef Obj(classIdx) -> DexClassData(DexClassDataHeader & directMethods & virtualMethods) -> DexClassDataHeader(2 type of method size) -> DexMethod(methodIdx & codeOff) -> DexMethodId(nameIdx) -> Get Method Name
        #                                                                                                                                                                              -> DexCode -> Get method message & ins

        #DexHeader(classDefsSize & classDefsOff)
        classDefSize = dexHeader.classDefSize
        classDefOff = dexHeader.classDefOff

        for i in range(0,classDefSize):
            offset = classDefOff + i * 0x20
            #DexClassDef(classIdx)
            classDefClassIdx = DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.mapfile[offset:offset+4],4),4)

            # DexTypeId(descriptorIdx)
            typeOffset =  classDefClassIdx * 4 + dexHeader.typeIdxOff

            #DexStringId(stringDataOff)
            classDefItemStringIdx = DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.mapfile[typeOffset:typeOffset+4],4),4)

            stringOffset = 4 * classDefItemStringIdx + dexHeader.stringIdxOff
            stringDataOff = DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.mapfile[stringOffset:stringOffset+4],4),4)

            strLen = ord(self.mapfile[stringDataOff])
            strClass = ""
            for j in range(0,strLen):
                strClass += self.mapfile[stringDataOff + 1 + j]

            conti = 0
            strAndroidSupport = "Landroid/support/"
            for ci in range(0,len(strAndroidSupport)):
                if strAndroidSupport[ci] != strClass[ci]:
                    conti = 1
                    break
            if conti == 0:
                continue

         #   print "--DbIF-- Class: " + strClass

            offset += 0x18                                                                                      #To the DexClassDataDef.classDataOff
            list_tmp = []
            for k in range(0,4):
                tmp = ord(self.mapfile[offset+k])
                list_tmp.append(tmp)

            classDataItem = DexFormAnalyzer.endianToNormal(list_tmp,4)
            if classDataItem == 0x0:
                continue
            dexClassDataHeader = DexFormAnalyzer.DexClassDataHeader(self.mapfile,classDataItem)

            classDataItemPointer = classDataItem + dexClassDataHeader.headerTakeBits

            #ignore field
            classDataItemPointer = self.jumpToNextField(self.mapfile,classDataItemPointer,dexClassDataHeader.staticFieldsSize,2)        #DexField has 2 fields
            classDataItemPointer = self.jumpToNextField(self.mapfile,classDataItemPointer,dexClassDataHeader.instanceFieldsSize,2)
            classDataOffset = classDataItemPointer

            classDataOffset = self.LoadMethod(classDataOffset,dexClassDataHeader.directMethodsSize,dexHeader,"Direct",strClass)
            self.LoadMethod(classDataOffset,dexClassDataHeader.virtualMethodsSize,dexHeader,"Virual",strClass)

    def LoadMethod(self,classDataOffset,methodsSize,dexHeader,methodType,strClass):
        listNumberAndValueBase = 0
        for methodNum in range(0,methodsSize * 3):
            listNumberAndValue = DexFormAnalyzer.analyzeleb128(self.mapfile,classDataOffset)
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
                stringIdx = DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.mapfile[methodIdxImp:methodIdxImp+4],4),4) * 4 + dexHeader.stringIdxOff
                stringIdxImp = DexFormAnalyzer.endianToNormal(DexFormAnalyzer.stringListToIntList(self.mapfile[stringIdx:stringIdx+4],4),4)
                stringlen = ord(self.mapfile[stringIdxImp])
                str = ""
                for strNum in range(0,stringlen):
                    str += self.mapfile[stringIdxImp+strNum+1]
              #  print "--DbIF-- " + methodType +" Method: " + str

            #analyze dex method code
            if (methodNum+1) % 3 == 0:
                if listNumberAndValue[1] != 0:
                    self.GetDexMethod(listNumberAndValue[1],strClass,str)
        return classDataOffset

    def GetDexMethod(self,offset,className,methodName):
        dexCode = DexFormAnalyzer.DexCode(offset,self.mapfile)
        self.dexMethodCodes.append(dexCode)
        self.dexClassName.append(className)
        self.dexMethodName.append(methodName)
