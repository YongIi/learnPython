# 开发人员：leo
# 开发时间：2022/10/7 14:42

"""
Bug的常见分类：
3、思路不清晰导致的问题，例如：

solution：
debug时：
（1）多使用print()函数
（2）多使用"#"暂时注释掉部分代码

4、被动掉坑
程序代码逻辑没有错，只是因为用户错误操作或者一些'例外情况'而导致的程序崩溃

solution:
Python提供了异常处理机制，可以在异常出现时及时捕获，然后内部"消化"，让程序继续运行

Python的异常处理机制：
将可能会出现异常的代码放在try：中
except xxx: 捕获可能出现的异常与报错（xxx可以省略），在冒号后给出报错后执行的代码

多个except结构：
捕获异常的顺序按照先子类后父类的顺序，为了避免一楼可能出现的异常，可以在最后增加BaseException

try...except...else...finally结构
如果try代码块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块，else块的内容就不会执行了
except和else是二选一执行的
finally块无论程序是否发生异常都会被执行，通常用来释放try块中申请的资源，例如：文件的关闭，数据库的链接都会放在finally块中
没有异常时，运行try...else...finally...
抛出异常时，运行try...except...finally...


"""
try:
    a = int(input("请输入第一个整数："))
    b = int(input("请输入第二个整数："))
    result = a / b
    print("结果为：", result)

except ZeroDivisionError:
    print("除数不能为0哦！！！")
except ValueError:
    print("只能输入数字串！！！")
print('程序结束')

print('-------------------------')

try:
    n1=int(input("请输入第一个整数："))
    n2=int(input("请输入第二个整数："))
    result = n1/n2
except BaseException as e:  # 也不知道会出现什么异常，将所有可能出现的报错异常都进行捕获，为BaseException，报错时的别名起为e
    print("出错了")
    print(e)
else:
    print("结果为：", result)
finally:
    print("谢谢您的使用")

print("程序结束")