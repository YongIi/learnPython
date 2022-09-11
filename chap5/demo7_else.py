# 开发人员：leo
# 开发时间：2022/9/5 15:29

# 与else语句配合使用的三种情况
'''
1，与if配合使用，if条件表达式不成立时执行else
2，与while配合使用，没有碰到break时执行，在循环的正常执行次数完成后执行else
'''

for item in range(3):
    pwd = input("请输入密码：")
    if pwd == "666":
        print("密码正确")
        break
    else:
        print("密码错误")
else:
    print("对不起，3次密码均输入错误")

a = 0
while a < 3:
    pwd = input("请输入密码：")
    if pwd == "888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a += 1
else:
    print("对不起，3次密码均输入错误")
