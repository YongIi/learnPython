# 开发人员：leo
# 开发时间：2022/9/3 17:21

# 条件表达式
"""
x if 判断条件 else y
如果判断条件为True，则条件表达式的返回值为x，否则返回y
"""

"""
输入两个整数比较大小
"""

num_a = int(input("请输入第一个整数：\n"))
num_b = int(input("请输入第二个整数：\n"))

# 正常写法
'''
if num_a >= num_b:
    print(num_a, ">=", num_b)
else:
    print(num_a, "<", num_b)
'''

# 使用条件表达式进行比较
print("num_a" + " >= " + "num_b" if (num_a >= num_b) else "num_a" + " < " + "num_b")  # 使用”“是为了把整数转化为字符串，也可以用str()，拼接符+只能连接字符串
