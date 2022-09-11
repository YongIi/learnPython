# 开发人员：leo
# 开发时间：2022/9/5 14:30

# break语句：用于结束循环语句，通常与if一起使用

'''
从键盘录入密码，最多3次，如果正确就结束循环
'''

for _ in range(3):
    pwd = input("请输入密码：")
    if pwd == "666":
        print("密码正确")
        break
    else:
        print("密码不正确")

a = 0
while a < 3:
    pwd = input("请输入密码：")
    if pwd == "888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a+=1