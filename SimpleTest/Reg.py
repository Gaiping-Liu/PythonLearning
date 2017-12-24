#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_

import re


def IsMatch(s, p):
    # return re.sub(p, '', s, 1) == ''
    return re.fullmatch(p, s) != None


print(IsMatch('aa', 'a'))
print(IsMatch('aa', 'aa'))
print(IsMatch('aaa', 'aa'))
print(IsMatch('aa', 'a*'))
print(IsMatch('aa', '.*'))
print(IsMatch('ab', '.*'))
print(IsMatch('aab', 'c*a*b'))

pp = '(?P<value>\d+)'
ss = 'A123BC78D45'
m = re.findall(pp, ss)
for mi in m:
    print(mi)
print(re.search(pp, ss).groups())


def NewID():
    n = 0
    while True:
        yield str(n).rjust(10, '0')
        n = n + 1


# value = int(match.group('value'))
#    return str(value)

def ReOrder(oldOrderList):
    n = NewID()
    for i in range(len(oldOrderList)):
        oldOrderList[i] = next(n)
    return oldOrderList


oldList = ['9', '7', '6', '10', '12', '5']
print(ReOrder(oldList))
