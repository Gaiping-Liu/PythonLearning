# _*_ coding: utf-8 _*_

names = ['a', 'b', 'c']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
print(sum)

alist = list(range(5))
alist = list(range(101))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('Hello, %s!' % name)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 1
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

    # 死循环时： ctrl+c 退出程序
