# 开发人员：leo
# 开发时间：2022/9/12 14:15

# 字典生成式

"""
要求：
items = ["Fruits", "Books", "Others"]
prices = [96, 78, 85]
将第一个列表中的元素作为键
将第二个列表中的元素作为值

打包内置函数zip()，将两个列表中对应的元素打包成一个元组，这些元组可以用list()组成列表。当两个列表的元素个数不相等时，取最小个数

{item.upper(): price for item, price in zip(items, prices)}  # .upper()只是控制大小写
该行表达式的含义见"字典生成式.png"
"""

items = ["Fruits", "Books", "Others"]
prices = [96, 78, 85]
lst = zip(items, prices)
print(lst, type(lst))
print(list(lst))

d = {item: price for item, price in zip(items, prices)}
print(d)

# 还可以在键后面添加.upper()实现所有字母大写或是.title()实现首字母大写

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)

del d["BOOKS"]  # 删除单个元素
print(d)

del d  # 删除整个字典
# print(d)