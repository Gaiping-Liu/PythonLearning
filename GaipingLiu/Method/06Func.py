# _*_ coding: utf-8 _*_
import math

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


def my_quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("%s is not number", a)
    if not isinstance(b, (int, float)):
        raise TypeError("%s is not number", b)
    if not isinstance(c, (int, float)):
        raise TypeError("%s is not number", c)
    if a == 0:
        return -(c / b)
    elif (b ** 2 - 4 * a * c) < 0:
        return None
    else:
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


print(my_quadratic(2, 3, 1))
print(my_quadratic(1, 3, -4))

'''
位置参数 power(x,n) requires 2 params
默认参数 power(x,n=2) requires 2 params, but when no n, it will use n=2 as default, 
    that makes power(5) is same as power(5,2)
    必选参数必须在默认参数前面
    当有多个参数的时候，把变化大的参数放前面，变化小的参数放后面
'''


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll("Bob", 'M', 7)  # 多个默认参数调用时，按照顺序提供默认参数
enroll("Adam", 'M', city="Tianjin")  # 不按照顺序提供默认参数是，需要把参数名写上

'''
默认参数必须指向不变对象，如果默认参数是可变对象，那么在第一次调用默认参数时，默认参数的对象就被更改了，
下一次再调用到默认参数，那么就已经是被更改了的默认参数，如下1
'''


def add_end1(L=[]):
    L.append('END')
    return L


print(add_end1())
print(add_end1())  # here the value of default L has changed by above
print(add_end1())  # here the value of default L has changed by above


def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end2())
print(add_end2())  # this will always correct as not changed by above

'''
定义可变参数 用* 放在可变参数前
'''


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 用 list or tuple 调用可变参数方法，可以加* 调用
nums = [1, 2, 3]
print(calc(*nums))  # *nums 表示把nums 这个list 的所有元素作为可变参数传进去

'''
关键字参数：允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成为一个dict
如下**extra 调用，**extra表示把extra这个dict的所有key-value用关键字参数传入**kw参数，
kw获得的dict是extra的一份copy，对kw的改动不会影响函数外的extra。
'''


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Bob', 35, city='beijing'))
print(person('Bob', 35, city='beijing', gender='M'))  # 用户注册实现可选功能

extra = {'city': 'beijing', 'job': 'engineer'}
print(person('Jack', 24, **extra))  # 将一个dict 作为关键字参数传入函数


def product(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum


print(product(5))
print(product(5, 6))
print(product(5, 6, 7))
print(product(5, 6, 7, 9))


# 递归函数需要注意防止栈溢出， fact(1000) 就会溢出
def factbad(n):
    if n == 1:
        return 1
    return n * factbad(n - 1)


'''
解决递归调用栈溢出的方法是通过尾递归优化。（循环可以看成是一种特殊测尾递归函数）
尾递归是指，再函数返回的时候，调用自身本身，并且return 语句不包含表达式
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
遗憾的是，大多数编程语言并没有针对尾递归做优化，Python解释器也没有做优化，所以，即使如下fact（n) 函数改成尾递归方式，也会导致栈溢出。
'''


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# print(fact(10000))

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'a', 'b', 'c')

#this is a test