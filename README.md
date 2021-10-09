# DexScanner
DEX中检查特定API调用处，该工程里只添加了dexClassLoader的检测
代码没有怎么写注释，如需添加扫描其他API，可以看看我CSDN上的一些说明（https://blog.csdn.net/u011247544/article/details/61922270?spm=1001.2014.3001.5501）

支持单文件/文件夹导入进行扫描
支持包含APK路径下对odex文件的扫描（apk不包含dex的前提）

使用方式：
命令行执行main.py,输入目标APK（或者文件夹）的路径，自动遍历APK，在桌面生成日志。
扫描指令编写参考main.py:
    rule1 = Rules(FIND_CALL_DIRECT_METHOD, methodName="<init>", className="Ldalvik/system/DexClassLoader;")
    rule2 = Rules(FIND_CALL_VIRTUAL_METHOD, methodName="loadClass")
    rule3 = Rules(FIND_CALL_STATIC_METHOD, methodName="format", className="Ljava/lang/String;")
    rule4 = Rules(FIND_PUT_STRING, stringValue="yyyy_MM_dd_HH_mm_ss")
    rule5 = Rules(FIND_PUT_VALUE, value=0x1d4c0)            #整型
    rule6 = Rules(FIND_PUT_VALUE, value=0x10000000)         #浮点型

注意：
获取桌面路径通过WINDOWS API，Linux下会有差异。
