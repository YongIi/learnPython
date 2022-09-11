# 开发人员：leo
# 开发时间：2022/9/6 10:13

# 列表的查询操作
"""
1、lst.index()获取列表中指定元素的索引
    如果列表中有N个相同的元素，只返回相同元素中第一个元素的索引
    如果查询的元素不存在，则程序运行报错，会抛出ValueError
    lst.index("hello", 1, 3)还可以再指定的start和stop之间进行查找，范围不包括stop

2、获取列表中的单个元素
    正向索引从0到N-1，eg:lst[0]
    逆向索引从-1到-N，eg:lst[-N]
    指定索引不存在，抛出IndexError
"""

lst = ["hello", "world", 98, "hello"]

print(lst.index("hello"))  # 如果列表中有N个相同的元素，只返回相同元素中第一个元素的索引

# print(lst.index("hello222"))  # ValueError: 'hello222' is not in list

# print(lst.index("hello", 1, 3))  # 范围不包括stop  ValueError: 'hello' is not in list

print(lst.index("hello", 1, 4))

print(lst[3])

print(lst[-3])

# print(lst[10])  # IndexError: list index out of range