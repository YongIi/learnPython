# 开发人员：leo
# 开发时间：2022/10/11 21:50

# 创建对象

"""
对象的创建又称为类的实例化

语法：
实例名 = 类名()  # 用类名()创建一个对象，由实例名指向该对象

在创建类时，类名是类对象；在创建对象时，类名()是实例对象，该实例对象由实例名指向。
如何知道该实例对象是属于某个类对象的呢？实例对象中有个类指针指向了该类对象，具体的数据结构看图《类对象和实例对象.png》

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
stu1 = Student("张三", 20)  # 用类名()创建一个对象，由实例名指向该对象
print(id(stu1))
print(type(stu1))  # <class '__main__.Student'> Student类型
print(stu1)  # <__main__.Student object at 0x0000022451790910> 就是id(stu1)地址的十六进制位置上的Student对象

print("--------")

print(id(Student))
print(type(Student))
print(Student)

# 使用对象
stu1.eat()  # 此处调用实例方法（函数）不需要为self传递对象，self就是指向stu1对象本身  # 对象名.函数名()
print(stu1.name)
print(stu1.age)
print("-----直接使用类名来访问类中的函数-----")
Student.eat(stu1)  # 此时需要为形参else指定实例对象，61行代码与57行代码的功能是相同的，都是调用Student类中的eat()函数  # 类名.函数名(对象名)

