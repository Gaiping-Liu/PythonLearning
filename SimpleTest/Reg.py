#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_

import re


def IsMatch(s, p):
    return re.sub(p, '', s, 1) == ''


print(IsMatch('aa', 'a'))
print(IsMatch('aa', 'aa'))
print(IsMatch('aaa', 'aa'))
print(IsMatch('aa', 'a*'))
print(IsMatch('aa', '.*'))
print(IsMatch('ab', '.*'))
print(IsMatch('aab', 'c*a*b'))
