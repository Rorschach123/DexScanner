__author__ = 'Rorschach'
# -*- coding: UTF-8 -*-

from DexHandler import DexFormAnalyzer, DexFormMap, DexFormDetect, DexFormLoader
from Utils.FileUtil import *

if __name__ == '__main__':
    apkPath = GetApkPath()
    apkList = []

    if os.path.isdir(apkPath):
        # dir:loop all files
        LoopDirFiles(apkPath, apkList, ".apk", 4)
    else:
        strLen = len(apkPath)
        if apkPath[strLen - 4:strLen] == ".apk":
            apkList.append(apkPath)

    #解析DEX文件
    for file in apkList:
        dexFormMap = DexFormMap.DexMap()
        dexFormLoader = DexFormLoader.DexLoader()
        dexFormAnalyzer = DexFormAnalyzer.DexAnalyzer()

        logging.info("[File]%s", file)
        unzipDir = GetDexPathByZipApk(file)
        if unzipDir == "":
            logging.error("[Fail]Not Found Unzip Dir")
            continue

        dexPath = unzipDir + "classes.dex"
        amTime = GetSaltTimeStr()

        #读取dex文件
        try:
            dexFormLoader.GetMapFile(dexFormMap,dexPath)
        except Exception as e:
            CleanFiles(dexPath,amTime)
            continue

        #analyze dex file
        dexHeader = DexFormAnalyzer.DexHeaderProperty(dexFormLoader.mapfile)
        if not dexHeader.verifyDex(dexFormLoader.mapfile):
            logging.error("[Fail]dex file verify error.")
            exit(-1)

        dexFormLoader.LoadAllClassAndMethod(dexHeader)

        #Resolute ins
        dexDetect = DexFormDetect.DexDetect()
        dexDetect.SetDexLoaderObj(dexFormLoader)

        #Count number of set port
        countSetPort = dexDetect.DetectApkApi(dexHeader)


        CleanFiles(dexPath,amTime)
        del dexFormMap
        del dexFormLoader
        del dexFormAnalyzer
        gc.collect()
