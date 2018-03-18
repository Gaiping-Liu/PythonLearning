#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_

def FindLongestNonRepeatSubStringV1(str):
    target = ""
    tempstr = ""
    for tempchar in str:
        if tempchar not in tempstr:
            tempstr += tempchar
        else:
            if len(target)<len(tempstr):
                target = tempstr
            tempstr = tempchar
    if len(target) < len(tempstr):
        target = tempstr
    return target

def FindLongestNonRepeatSubStringV2(str):
    charAndSubstrDic = {}
    charAndLengthDic = {}
    maxLen = 0
    for tempchar in str:
        if tempchar not in charAndSubstrDic.keys():
            tempList, tempLen = FindLongestStrInList(str.split(tempchar))
            charAndSubstrDic[tempchar] = tempList
            charAndLengthDic[tempchar] = tempLen
            maxLen = maxLen if maxLen>=tempLen else tempLen
    targetList = []
    for key in charAndLengthDic.keys():
        if charAndLengthDic[key] == maxLen:
            for value in charAndSubstrDic[key]:
                targetList.append(value+key if value + key in str else key+value)
    return targetList

def FindLongestStrInList(lista):
    tempLen = 0
    listb=[]
    for str in lista:
        if len(str)>tempLen:
            tempLen = len(str)
            listb.clear()
            listb.append(str)
        elif len(str) == tempLen:
            listb.append(str)
    return listb, tempLen

# 后缀数组的最长前缀即为字符串中最长的无重复的子字符串
def FindLongestNonRepeatSubString(str):
    resultList = []
    maxLen = 0
    for i in range(len(str)):
        tempstr=FindLongestNonRepeatPrefix(str[i:]) # 后缀字符串为str[i:]
        if maxLen== len(tempstr):
            resultList.append(tempstr)
        elif maxLen< len(tempstr):
            maxLen = len(tempstr)
            resultList.clear()
            resultList.append(tempstr)
    return resultList
def FindLongestNonRepeatPrefix(str):
    prefix = ''
    for i in range(len(str)):
        if str[i] not in prefix:
            prefix +=str[i]
        else:
            break
    return prefix

str = "abcabcd"
print(FindLongestNonRepeatSubStringV1(str))

for substr in FindLongestNonRepeatSubStringV2(str):
    print(substr)
    
for substr in FindLongestNonRepeatSubString(str):
    print(substr)