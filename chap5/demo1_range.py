# 开发人员：leo
# 开发时间：2022/9/4 16:21

# range()  生成一个整数序列，不管range对象表示的序列有多长，所有range对象所占内存空间是相同的，因为只需要存储start、stop、step
# 只有当用到range对象时才计算序列中的相关元素，可以用in、not in判断序列中是否存在指定的整数
# 返回值是一个迭代器对象，不会看到序列中具体的数据，但可以用list查看range对象中的整数序列，list是列表
# range(start,stop,step)    其中start和step可以省略，start省略时为0，step省略时其值为1，序列的长度为stop-start

r = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 从0开始，到10结束但不包含10
print(r)  # range(0, 10)
print(list(r))  # 可以用list查看range对象中的整数序列，list是列表

r = range(1, 10)  # 从1开始，到10结束但不包含10
print(r)  # range(1, 10)
print(list(r))

r = range(1,10,2)  # 从1开始，步长为2，到10结束但不包含10
print(r)  # range(1, 10, 2)
print(list(r))  # [1, 3, 5, 7, 9]

"""
判断指定的值是否在序列中是否存在
"""

print(8 in r)
print(9 not in r)