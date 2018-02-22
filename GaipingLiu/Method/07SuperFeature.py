# _*_ coding: utf-8 _*_

# Slice 切片
L = ['michael', 'sarah', 'tracy', 'bob', 'jack']
print(L[0:3])  # 切片取list 的前三个元素，表示从索引0开始，到索引3结束，但不包括索引3
print(L[:3])  # 如果第一个索引是0， 可以省略
print(L[1:3])
print(L[-2:])  # 取倒数第二个元素知道结尾
print(L[-2:-1])  # 倒数第一个元素为 -1， 取不到

L = list(range(100))
print(L[:10])  # 取前十个
print(L[-10:])  # 取后十个
print(L[10:20])  # 取第10到第19个
print(L[:10:2])  # 前10个每隔2个取一个
print(L[::5])  # 所有数每隔5个取一个
print(L[:])  # 原样复制了一个list L

print((0, 1, 2, 3, 4, 5)[:3])  # tuple 也可以切片，结果仍然是tuple
print('ABCDEG'[:3])  # string 也可以切片，结果仍然是string


def trim(s):
    print(s)
    print(s.find('\s*'))
    print(s.find('\s*$') - 1)
    print(s[s.find('^\s*'):s.find('\s*$') - 1])


trim("    abc  ")
