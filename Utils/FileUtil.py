__author__ = 'Rorschach'
# -*- coding: UTF-8 -*-

import sys,logging,re,zipfile,time,os,shutil,winreg,gc,random
logging.basicConfig(format='[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s]%(message)s', level=logging.DEBUG)

#通过参数传入或者通过命令行输入APK路径
def getApkFilePath():
    apklist = []

    if len(sys.argv) > 1:
        apklist.append(sys.argv[1])
    else:
        arg1 = input("input apk file path:")
        apklist.append(arg1)

    return apklist

#获取APK路径
def getApkPath():
    listArgv = getApkFilePath()
    apkPath = listArgv[0]

    if apkPath == "":
        logging.error("[Fail]GetApkPath")
        exit(-1)

    return apkPath

#解压APK得到DEX
def getDexPathByZipApk(apkPath):
    unzipDirPath =  unzipFile(apkPath, getDesktop())
    if unzipDirPath == "":
        logging.error("[Fail]unzip classes.dex")
        return ""
    else:
        # logging.info("[Success]unzip dex : %s", unzipDirPath)
        return unzipDirPath

#从odex中查找dex
def findDexFileInOdex(unzipPath, apkPath):
    strlen = len(apkPath)
    while strlen != 0:
        if apkPath[strlen-1:strlen] == "\\":
            apkPath = apkPath[0:strlen]
            break
        strlen -= 1
    odexList = []
    loopDirFiles(apkPath, odexList, ".odex", 5)
    if len(odexList) == 1:
        #cp file to unzipPath,cut before dex
        open(unzipPath+"classes.dex", "wb").write(open(odexList[0], "rb").read())
        ret = fixOdexToDex(unzipPath + "classes.dex")
        return ret
    return 0

#从odex中提取dex
def fixOdexToDex(dexFile):
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
    except Exception as e:
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

#遍历目录下所有文件
def loopDirFiles(path, fileList, keyStr, lens):
    files = os.listdir(path)
    for file in files:
        filePath = os.path.join(path,file)
        if os.path.isdir(filePath):
            loopDirFiles(filePath, fileList, keyStr, lens)
        else:
            strLen = len(filePath)
            if filePath[strLen-lens:strLen] == keyStr:
                fileList.append(filePath)

#删除解压文件
def cleanFiles(dexPath):
    logging.info("[Delete]" + dexPath)
    if os.path.isdir(dexPath):
        shutil.rmtree(dexPath)

    # pathList = dexPath.split("/")
    # for listNum in range(0,(len(pathList) - 1)):
    #     dexDirPath = dexDirPath + pathList[listNum] + "/"

#仅获取WINDOWS桌面目录
def getDesktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]

#获取时间+随机值避免重复
def getSaltTimeStr():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + str(random.randint(0, 99999999))

#解压zip包,返回解压后的文件夹路径
def unzipFile(path, unzipPath):
    isZip = zipfile.is_zipfile(path)
    starttime = getSaltTimeStr()
    extractPath = unzipPath + "/" + starttime + "/"

    if isZip:
        filezip = zipfile.ZipFile(path,'r')
        for file in filezip.namelist():
            if file.startswith("classes") and file.endswith(".dex"):
                if not os.path.isdir(extractPath):
                    os.makedirs(unzipPath + "/" + starttime)
                filezip.extract(file, extractPath)
    else:
        logging.error("[Fail]Not Zip File")

    return extractPath
