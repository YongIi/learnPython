# 开发人员：leo
# 开发时间：2022/10/7 17:15

# Python中常见的异常类型

"""
1、ZeroDivisionError  除（或取模）零 （所有数据类型）
2、IndexError 序列中没有此索引（index）
3、KeyError  映射中没有这个键
4、NameError 未声明/初始化对象（没有属性）
5、SyntaxError 语法错误
6、ValueError  传入无效的参数

"""

# 1、除0，数学运算异常
# print(10/0)

# 2、indexError
lst = [1, 2, 3, 4]
# print(lst[4])  # 索引是从0开始的

# 3、KeyError
dic = {"name": "张三", "age": 20}
# print(dic["gender"])

# 4、NameError
# print(num)  # num未定义

# 5、SyntaxError
# int a=20  # Python中变量是没有数据类型的，变量全是指针，指向另一个对象

# 6、ValueError 传入无效
# a=int('hello')
