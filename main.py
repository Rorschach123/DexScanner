__author__ = 'Rorschach'
# -*- coding: UTF-8 -*-

from DexHandler import DexFormAnalyzer, DexFormMap, DexFormLoader
from Utils.FileUtil import *
from DetectRules import Detecter

if __name__ == '__main__':
    apkPath = getApkPath()
    apkList = []

    if os.path.isdir(apkPath):
        loopDirFiles(apkPath, apkList, ".apk", 4)
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
        unzipDir = getDexPathByZipApk(file)
        if unzipDir == "":
            logging.error("[Fail]Not Found Unzip Dir")
            continue

        dexPath = unzipDir + "classes.dex"
        amTime = getSaltTimeStr()

        #读取dex文件
        try:
            dexFormLoader.getMapFile(dexFormMap, dexPath)
        except Exception as e:
            cleanFiles(dexPath, amTime)
            continue

        #解析dex文件
        dexHeader = DexFormAnalyzer.DexHeaderProperty(dexFormLoader.mapfile)
        if not dexHeader.verifyDex(dexFormLoader.mapfile):
            logging.error("[Fail]dex file verify error.")
            exit(-1)

        #加载dex中的类和方法
        dexFormLoader.loadAllClassAndMethod(dexHeader)

        #开始检测和扫描指定API
        dexDetect = Detecter.Detecter()
        dexDetect.detectApkApi(dexFormLoader, dexHeader)

        cleanFiles(dexPath, amTime)
        del dexFormMap
        del dexFormLoader
        del dexFormAnalyzer
        gc.collect()
