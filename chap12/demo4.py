# 开发人员：leo
# 开发时间：2022/10/11 17:41

# 类的创建

"""
1、创建语法
clss 类名:  # 类名是类对象，实例化后的对象是实例对象
    pass

2、类的组成
a. 类属性
直接定义在类里的变量称为类属性
b. 实例方法
其实就是函数，只是写在类里面称为‘实例方法’，形参必须有(self)，self类似与C++中的this指针
c. 静态方法
采用@staticmethod修饰的方法（函数），形参不允许有(self)
d. 类方法
采用@classmethod修饰的方法（函数）,形参必须有(cls)，cls就是class
e. init初始化方法
是b实例方法的变种，函数名用__init__(self, 其他形参)，类似于C++中的构造函数，用来初始化对象，被初始化的类变量（属性）称为实例属性
eg： self.name = name # self.name称为实例属性，与C++不同的是，不需要在类里面再额外定义实例属性，在Python中实例属性属于每个实例对象，是私有的；而其他各个方法(函数)和类属性是公有的

最好就把上面的各个函数称为：实例函数、静态函数、类函数。写在类外的称为函数，写在类里的称为方法
上面的变量称为：类属性、实例属性
"""


class Student:  # Student为类名，类名可以由一个或者多个单词组成，每个单词的首字母大写，其余小写（就是驼峰写法）
    # 类属性
    native_place = '湖南'  # 直接写在类里的变量，称为类属性

    # 实例方法。在类外定义的称为函数，在类内定义的称为方法
    def eat(self):
        print("学生在吃饭...")

    # 静态方法
    @staticmethod
    def method():  # 在静态方法中不允许使用self
        print("使用了staticmethod修饰，是静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print("使用了classmethod修饰，是类方法")

    # init初始化方法
    def __init__(self, name, age):  # 就是实例方法，只是函数名必须是__init__(self, 形参)，类似于C++中的构造函数，用来初始化对象
        self.name = name  # 被初始化的类变量（属性）称为实例属性，self.name称为实例属性，将形参的值（局部变量）传递给实例属性
        self.age = age  # 实例对象，一般Python中局部对象和实例属性名称是相同的


def drink():  # 定义在类外是函数
    print("喝水")
