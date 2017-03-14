__author__ = 'Rorschach'

import sys,re,zipfile,time,os,shutil,_winreg,gc,random
import DexFormMap,DexFormLoader,DexFormAnalyzer,DexFormDetect

def GetDesktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return _winreg.QueryValueEx(key, "Desktop")[0]

def GetFilePath():
    list = []
    if len(sys.argv) > 1:
        list.append(sys.argv[1])
    else:
        arg1 = raw_input("please input apk file path:\n")
        #arg1 = TransString(arg1)
        list.append(arg1)
    return list

def RetDexPathByCmd():
    listArgv = GetFilePath()
    dexPath = listArgv[0]
    if dexPath == "":
        print "--Fail-- Ret file path "
        exit(-1)
    print "--Sucs-- Ret file path "
    return dexPath

def RetDexPathByZipApk(apkPath):
    unzipDirPath =  UnzipFile(apkPath,GetDesktop())
    if unzipDirPath == "":
        print "--Fail-- Fail to unzip classes.dex"
        return ""
    else:
        print "--Succ--"
        return unzipDirPath

def GetSaltTimeStr():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + str(random.randint(0, 99999999))

def UnzipFile(path,unzipPath):
    isZip = zipfile.is_zipfile(path)
    starttime =  GetSaltTimeStr()
    hasFindAM = 0
    hasFindDex = 0
    if isZip:
        filezip = zipfile.ZipFile(path,'r')
        for file in filezip.namelist():
            if file == "classes.dex":
                if not os.path.isdir(unzipPath+"/"+ starttime +"/"):
                    os.makedirs(unzipPath+"/"+ starttime)
                filezip.extract(file,unzipPath+"/"+ starttime +"/")
                print "--Succ--  UnZip classes.dex Success"
                hasFindDex += 1
            if file == "AndroidManifest.xml":
                if not os.path.isdir(unzipPath+"/"+ starttime +"/"):
                    os.makedirs(unzipPath+"/"+ starttime)
                filezip.extract(file,unzipPath+"/"+ starttime +"/")
                print "--Succ--  UnZip AndroidManifest.xml Success"
                hasFindAM += 1
    else:
        print "--Fail-- Not Zip File"
    if hasFindDex == 0:
        hasFindDex = FindDexFileInOdex(unzipPath + "/" + starttime + "/",path)

    if hasFindDex == 1 and hasFindAM == 1:
        return unzipPath + "/" + starttime + "/"
    else:
        if os.path.isdir(unzipPath + "/" + starttime + "/"):
            shutil.rmtree(unzipPath + "/" + starttime + "/")
    return ""

def FindDexFileInOdex(unzipPath,apkPath):
    strlen = len(apkPath)
    while strlen != 0:
        if apkPath[strlen-1:strlen] == "\\":
            apkPath = apkPath[0:strlen]
            break
        strlen -= 1
    odexList = []
    LoopDirFiles(apkPath,odexList,".odex",5)
    if len(odexList) == 1:
        #cp file to unzipPath,cut before dex
        open(unzipPath+"classes.dex", "wb").write(open(odexList[0], "rb").read())
        ret = FixOdexToDex(unzipPath+"classes.dex")
        return ret
    return 0

def FixOdexToDex(dexFile):
    try:
        file = open(dexFile,"rb")
        f = file.read()
        cutOffset = 0
        for i in range(0,len(f)):
            if ord(f[i]) == 0x64 and ord(f[i+1]) == 0x65 and ord(f[i+2]) == 0x78 and ord(f[i+3]) == 0x0A:
                cutOffset = i
                break
        file.seek(0,2)
        fileSize = file.tell()
        file.seek(cutOffset,0)
        basePointer = []
        for j in range(cutOffset,fileSize):
            ch = file.read(1)
            basePointer.append(ch)
    except Exception,e:
        return 0
    finally:
        file.close()
    os.remove(dexFile)
    try:
        classFile = open(dexFile,"wb")
        for j in basePointer:
            classFile.write(j)
    finally:
        classFile.close()
    return 1

def LoopDirFiles(path,fileList,keyStr,lens):
    files = os.listdir(path)
    for file in files:
        filePath = os.path.join(path,file)
        if os.path.isdir(filePath):
            LoopDirFiles(filePath,fileList,keyStr,lens)
        else:
            strLen = len(filePath)
            if filePath[strLen-lens:strLen] == keyStr:
                fileList.append(filePath)

#remove unzip file
def CleanFiles(dexPath,amTime):
    pathList = dexPath.split("/")
    dexDirPath = ""
    for listNum in range(0,(len(pathList) - 1)):
        dexDirPath = dexDirPath + pathList[listNum] + "/"
    if os.path.isdir(dexDirPath):
        shutil.rmtree(dexDirPath)

if __name__ == '__main__':
    print "--------------Start Main Func------------------"
    #get file path list:
    apkPath = RetDexPathByCmd()
    apkList = []

    if os.path.isdir(apkPath):
    #dir:loop all files
        LoopDirFiles(apkPath,apkList,".apk",4)
    else:
        strLen = len(apkPath)
        if apkPath[strLen-4:strLen] == ".apk":
            apkList.append(apkPath)

    try:
        logFileName = GetDesktop()+"\\log-" + GetSaltTimeStr()
        logFile = open(logFileName,"w+")
        oldStdOut = sys.stdout
        sys.stdout = logFile
    finally:
        r0 = 0

    #analyze dex file path
    for file in apkList:
        dexFormMap = DexFormMap.DexMap()
        dexFormLoader = DexFormLoader.DexLoader()
        dexFormAnalyzer = DexFormAnalyzer.DexAnalyzer()

        print "File :" + file
        print "--Load-- Get dex file path"
        unzipDir = RetDexPathByZipApk(file)
        if unzipDir == "":
            print "--Fail-- Not Found Unzip Dir"
            continue

        dexPath = unzipDir + "classes.dex"
        amTime = GetSaltTimeStr()

        #read dex file
        print "--Load-- Read Dex file"
        try:
            dexFormLoader.GetMapFile(dexFormMap,dexPath)
        except Exception,e:
            CleanFiles(dexPath,amTime)
            continue

        #analyze dex file
        dexHeader = DexFormAnalyzer.DexHeaderProperty(dexFormLoader.mapfile)
        dexFormLoader.LoadAllClassAndMethod(dexHeader)

        #Resolute ins
        dexDetect = DexFormDetect.DexDetect()
        dexDetect.SetDexLoaderObj(dexFormLoader)

        #Count number of set port
        print "--------------------------------------------------------------------------"
        countSetPort = dexDetect.DetectApkApi(dexHeader)
        print "--------------------------------------------------------------------------"


        CleanFiles(dexPath,amTime)
        print ""
        del dexFormMap
        del dexFormLoader
        del dexFormAnalyzer
        gc.collect()

    if logFile:
        logFile.close()
    if oldStdOut:
        sys.stdout = oldStdOut
    print "--------------Finish Main Fnc------------------"
    os.system('pause')

#r"C:\Users\Rorschach\Desktop\MI5\sapp\AntHalService\AntHalService.apk"