# _*_ coding: utf-8 _*_

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')

# if 判断条件简写如下，只要X 是非零数值，非空字符串，非空list等，就判断为True， 否则判断为False
x = 10
if x:
    print('True')
birth = input('input: ')
# input got from here is str, need do convert to int to compare with 2000 below
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5
bmi = (weight / height) ** 2
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
