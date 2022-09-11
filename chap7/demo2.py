# 开发人员：leo
# 开发时间：2022/9/7 15:15

# 获取字典中的元素
"""
1、用方括号[键]
eg：
scores["张三"]
2、使用get()函数
eg:
scores.get("张三")

区别：
1、使用方括号[键]，如果字典中不存在指定的key，抛出keyError异常
2、使用get()函数取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None，
可以通过get("不存在的键", defaltValue)参数设置默认的value，以便指定的key不存在时返回

"""

scores = {"张三": 100, "李四": 98, "王五": 45}
print(scores["张三"])
print(scores.get("张三"))

# print(scores["陈六"])  # KeyError: '陈六'
print(scores.get("陈六"))  # None
print(scores.get("麻七", 99))  # 99是在查找"麻七"所对应的value不存在时，提供一个默认值