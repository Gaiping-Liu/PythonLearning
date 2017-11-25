#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_
print('this is a test')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print('包含中文的字符串')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
str1 = 'abc'
str2 = '中文'
str3 = b'abc'
str4 = b'\xe4\xb8\xad\xe6\x96\x87'
print(str1.encode('ascii'))
print(str2.encode('utf-8'))
print(str3.decode('ascii'))
print(str4.decode('utf-8'))
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))
print(len(str2.encode('utf-8')))
print('hello, %s' % 'world')
print('hi, %s, you have $%d.' % ('Michael', 10000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

s1 = 72
s2 = 85
improve = (s2 - s1) / s1
improve = '小明成绩提高了：%.1f%%' % (improve * 100)
print(improve)
