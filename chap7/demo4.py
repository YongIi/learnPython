# 开发人员：leo
# 开发时间：2022/9/12 12:51

# 字典的视图操作
"""
获取字典试图的三个方法
1. keys()       获取字典中所有key
2. values()     获取字典中所有value
3. items()      获取字典中所有key-value对


"""

scores = {"张三": 100, "李四": 98, "王五": 45}

# 获取所有的键

print(scores.keys(), type(scores.keys()))

print(list(scores.keys()))  # 可以通过list将所有key组成的试图转化为列表

# 获取所有的值

values = scores.values()
print(values)
print(type(values))
print(list(values))  # 通过list将values转化为列表

# print(scores.values(), type(scores.values()))

# 获取所有键值对
# print(scores.items(), type(scores.items()))
items = scores.items()
print(items)  # dict_items([('张三', 100), ('李四', 98), ('王五', 45)])  # []内是一组 元组
print(list(items))  # [('张三', 100), ('李四', 98), ('王五', 45)]  # 转化为list列表后，列表中每一个元素是一组元组

"""
自我总结
{"张三": 100, "李四": 98, "王五": 45}  是字典
其keys()转化为list后
['张三', '李四', '王五']  是列表
其values()转化为list后
[100, 98, 45]  也是列表
其items转化为list后
[('张三', 100), ('李四', 98), ('王五', 45)] 也是列表，但里面每一个元素都是 元组

字典用{}
列表用[]
元组用()
"""