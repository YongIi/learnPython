# 开发人员：leo
# 开发时间：2022/9/2 22:09

# python中一切皆是对象，所有对象都有一个bool值，可以用内置函数bool()获取对象的bool值
# 以下对象的bool值为false
# false 数值0.0 None 空字符串 空列表 空元组 空字典 空集合

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool("0"))
print(bool(None))
print(bool(""))
print(bool([]))  # 空列表
print(bool(list()))  # 空列表
print(bool(()))  # 空元组()
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合
