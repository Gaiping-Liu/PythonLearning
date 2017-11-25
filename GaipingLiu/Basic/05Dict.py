# _*_ coding: utf-8 _*_

d = {'a': 95, 'b': 75, 'c': 85}
print(d['a'])
print('d' in d)
# get() 如果key 不存在，返回None 或自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))
print(d.pop('b'))  # delete key 'b' and it's value from dict
'''
dict 根据key来计算value，这个通过key计算位置的算法成为哈希算法，为了保证hash 的正确性，key 的对象就不能变
在python 中，字符串，整数都是不可变的，因此可以作为key，而list 是可变的，就不能作为key
'''
# set 是key值不重复的list，set 是无序的, set 是无序的和无重复元素的集合，因此可以做数学意义上的交集、并集等操作
s = set([1, 1, 2, 2, 3, 3])
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
testDictTuple = {(1, 2, 3): 10, (2, 3): 5}
testSetTupe = set((1, 2, 3))
print(testDictTuple)
print(testSetTupe)
