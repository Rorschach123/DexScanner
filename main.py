__author__ = 'Rorschach'
# -*- coding: UTF-8 -*-

from DexHandler import DexFormAnalyzer, DexFormMap, DexFormLoader
from Utils.FileUtil import *
from DetectRules import *
from DetectRules.SmaliMarco import *

if __name__ == '__main__':
    apkPath = getApkPath()
    logging.info("[File]%s", apkPath)

    unzipDir = getDexPathByZipApk(apkPath)
    if unzipDir == "":
        logging.error("[Fail]Not Found Unzip Dir")
        exit(-1)

    dexlist = []
    loopDirFiles(unzipDir, dexlist, ".dex", 4)

    #制定需要扫描的方法\类\类型\变量
    rule1 = Rules(INS_INVOKE_DIRECT, CHECK_CLASS_TYPE, methodName="<init>", className="Ldalvik/system/DexClassLoader;")
    rule2 = Rules(INS_INVOKE_VIRTUAL, CHECK_METHOD_TYPE, methodName="loadClass")
    rules = [rule1, rule2]

    for dexPath in dexlist:
        logging.info("[Load]" + dexPath)
        #解析dex文件
        dexFormMap = DexFormMap.DexMap()
        dexFormLoader = DexFormLoader.DexLoader()
        dexFormAnalyzer = DexFormAnalyzer.DexAnalyzer()

        #读取dex文件
        try:
            dexFormLoader.getMapFile(dexFormMap, dexPath)
        except Exception as e:
            logging.error("[Load]%s error." %dexPath)
            continue

        #解析dex文件
        dexHeader = DexFormAnalyzer.DexHeaderProperty(dexFormLoader.mapfile)
        if not dexHeader.verifyDex(dexFormLoader.mapfile):
            logging.error("[Fail]dex file verify error.")
            exit(-1)

        #加载dex中的类和方法
        dexFormLoader.loadAllClassAndMethod(dexHeader)

        #开始检测和扫描指定API
        logging.info("[Detc]Start Detecting...")
        dexDetect = Detecter()
        dexDetect.detectApkApi(dexFormLoader, dexHeader, rules)
        logging.info("[Detc]Finish")

        del dexFormMap
        del dexFormLoader
        del dexFormAnalyzer
        gc.collect()

    #删除解压文件
    cleanFiles(unzipDir)
