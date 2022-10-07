# 开发人员：leo
# 开发时间：2022/10/7 14:08

# Bug的由来及分类

"""
最初是一只真实的虫影响了程序的运行，后来都用bug来指程序错误

相对应的是debug，即调试

Bug的常见分类：
1、粗心导致的语法错误SyntaxError
solution：
查找是否漏了末尾的冒号
查找是否缩进有错误
英文符合是否写成了中文符号，eg：: ( )
字符串拼接时，把字符串和数字拼在了一起
没有定义变量，例如while的循环条件的变量
比较运算符==与赋值运算符=混用
"""

# 粗心导致的语法错误
"""
age = input("请输入您的年龄：")
if age >= 18:
    print("成年人")
    
while i < 10:  # i没定义
    print(i)  # 死循环
    
for i in range(3):
    uname = input("请输入用户名：")
    pwd = input("请输入密码：")
    if umane = 'admin' and pwd = 'admin':
        print('登入成功')
        break
    else
        print("输入有误")
else
    print("对不起，三次均输入错误")    
"""
age = input("请输入您的年龄：")  # input函数输入的都是str类型
if int(age) >= 18:
    print("成年人")

i = 0
while i < 10:
    print(i)
    i += 1  # Python中没有i++和i--

for i in range(3):
    uname = input("请输入用户名：")
    pwd = input("请输入密码：")
    if uname == 'admin' and pwd == 'admin':
        print('登入成功')
        break
    else:
        print("输入有误")
else:
    print("对不起，三次均输入错误")

print("s"+ "123")