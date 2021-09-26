__author__ = 'Rorschach'
# -*- coding: UTF-8 -*-


def endianToNormal(byteArray,length):
    s = 0
    s1 = 1
    for letter in range(0,length):
        s += byteArray[letter] * s1
        s1 *= 0x100
    return s

def stringListToIntList(stringList,length):
    intList =[]
    for i in range(0,length):
        intList.append(ord(stringList[i]))
    return intList
