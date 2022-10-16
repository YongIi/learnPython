# 开发人员：leo
# 开发时间：2022/10/16 14:24

# object类

"""
1、object类是所有类的父类，因此所有类都有object类的属性和方法

2、内置函数dir(对象名)可以查看指定对象所有属性

3、object类有一个__str__(self)方法（函数），用于返回一个对于“对象的描述”，一般用于print(对象名)时调用该函数输出“对象的描述”
对应于内置函数str()经常用于print(对象名)方法，帮助我们查看对象的信息，所以我们经常会对__str__()进行重写
即对object类中的__str__(self)方法（函数）改写后，print(对象名)会调用重写后的__str__(self)函数，否则会调用object的__str__(self)，给出默认信息

"""

class Student:  # 默认继承object类
    def __init__(self, name, age):  # 重写object类的__init__()函数
        self.name = name
        self.age = age

    def __str__(self):  # 重写object类的__str__()函数
        return '我的名字是{0},今年{1}岁了'.format(self.name, self.age)

stu = Student("张三", 20)

print(dir(stu))

print(stu)  # 注意：默认会调用object类的__str__(self)，但子类改写__str__(self)后，输出的内容是改写后的__str__(self)函数
