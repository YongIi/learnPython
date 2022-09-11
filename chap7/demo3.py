# 开发人员：leo
# 开发时间：2022/9/11 21:56

# key的判断
"""
in 指定的key在字典中存在返回True  eg: "张三" in scores
not in 指定的key在字典中不存在返回True  eg: "Marry" not in scores

# 字典元素的删除
del scores["张三"]  # 删除指定的键-值对
scores.clear()  # 清空字典的元素

# 字典元素的新增
score["jack"] = 90  # 如果该键是存在的，则修改值

"""

scores = {"张三": 100, "李四": 98, "王五": 45}

print("张三" in scores)
print("Marry" not in scores)

del scores["张三"]  # 删除指定的键-值对
print(scores)
scores.clear()  # 清空字典的元素
print(scores)

scores["jack"] = 90
print(scores)

scores["jack"] = 95
print(scores)


