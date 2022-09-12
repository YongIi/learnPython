# 开发人员：leo
# 开发时间：2022/9/12 13:20

# 字典元素的遍历

"""
for 自定义迭代变量 in 字典:  # 其中自定义变量是字典的键key
    循环体

"""

scores = {"张三": 100, "李四": 98, "王五": 45}

for item in scores:  # item是字典元素的键
    print(item)
    print(scores[item], scores.get(item))  # 字典值的获取要用[]或者get()函数
