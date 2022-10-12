# 开发人员：leo
# 开发时间：2022/10/12 15:50

# 类属性、类方法（函数）、静态方法（函数）

"""
类属性：类中方法（函数）外的变量称为类属性，被该类的所有对象所共享，可以采用类名来调用，也可以通过对象调用
共享原因：所有该类实例化的对象都有一个类指针指向该类

类方法（函数）：使用@classmethod修饰的方法（函数名(cls)），调用时不需要传入(cls)参数，使用类名直接访问的方法（函数），（其实也可以通过对象访问）

静态方法（函数）：使用@staticmethod修饰的方法（函数），没有任何默认参数，使用类名直接访问的方法（函数），（其实也可以通过对象访问）

-------

实例方法（函数）：实例方法（函数名(self)）中首先传递的是实例的对象

"""


# 创建类
# 将上节课定义的类复制过来

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

# 创建对象
stu1 = Student("张三", 20)
stu2 = Student("李四", 30)

# 类属性的使用方式
print(Student.native_place)  # 方法一：使用类名调用
print(stu1.native_place)  # 方法二：使用对象调用
print(stu2.native_place)
Student.native_place = "安徽"
print(stu1.native_place)  # 方法二：使用对象调用
print(stu2.native_place)

print("-----类方法（函数）的使用方式-----")
Student.cm()  # 在调用的时候不需要传入(cls)参数
stu1.cm()

print("-----静态方法（函数）的使用方式-----")
Student.method()
stu1.method()