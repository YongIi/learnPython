# 开发人员：leo
# 开发时间：2022/9/6 14:45

# 判断指定元素在列表中是否存在
# 语法格式： 元素 in 列表名
# 语法格式： 元素 not in 列表名

# 列表元素的遍历
"""
for 迭代变量 in 列表名:
    操作
"""

print("p" in "python")  # True

lst = [10, 20, "hello", "python"]
print(10 in lst)  # True
print(100 in lst)  # False

print("-----遍历列表元素-----")
for item in lst:
    print(item)
