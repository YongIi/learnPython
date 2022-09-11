# 开发人员：leo
# 开发时间：2022/7/13 14:14

# 从键盘录入两个整数，并求和
a = input("请输入一个加数：")  # 输入值的类型是str，查看它也是str类型
# a = int(a)  # 将转换的结果存储在a中
b = input("请输入另一个加数：")
# b = int(b)
print(type(a), type(b))
print(a + b)  # 执行的是字符串的拼接
print(int(a) + int(b))
