# _*_ coding: utf-8 _*_

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))  # get the item counts in the list
print(classmates.count('tracy'))
for a in classmates:
    print(a)
print(classmates[-1])  # get the last item, -2 -3 also can be used
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
print(classmates.pop())  # delete the last item
print(classmates)
print(classmates.pop(1))
print(classmates)
Ltest = ['apple', 123, True]
print(Ltest)
Ltest2 = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(Ltest2))
print(Ltest2)
L = []
print(len(L))

'''Tuple 元组，一旦初始化就不能修改？所以当你在定义个时候，必须把tuple的元素确定下来
不能修改的是元素指向的地址，
如果tuple 的元素里包含list， 然而list 又是可以变的，所以这种tuple某种意义上是’可变‘的
'''
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# print(t=())
# To define a tuple with only one element, should use below grammar
testt = (1,)
print(testt)
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# print apple
print(L[0][0])
# print Python
print(L[1][1])
# print Lisa
print(L[2][2])
