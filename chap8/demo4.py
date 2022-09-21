# 开发人员：leo
# 开发时间：2022/9/21 14:30

# 元组的遍历

t = tuple(("Python", "hello", 90))

# 访问方式一：使用索引
print(t[0])
print(t[1])
print(t[2])
# print(t[3])  # IndexError: tuple index out of range

# 访问方式二：遍历元组
for item in t:
    print(item)
