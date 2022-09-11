# 开发人员：leo
# 开发时间：2022/9/7 14:13

# 列表生成式
"""
生成列表的公式
语法格式：

[表达式 for 自定义变量 in 可迭代对象]
[i*i for i in range(1, 10)]

表示列表元素的表达式中通常包含自定义变量，eg: i
"""

lst = [i * i for i in range(1, 10)]
print(lst)

# 列表元素为[2, 4, 6, 8, 10]
lst2 = [2*i for i in range(1, 6)]
