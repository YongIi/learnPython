# 开发人员：leo
# 开发时间：2022/10/15 19:32

# 继承

"""
继承可以提高代码的复用性
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法

语法格式：
class 子类名称(父类1, 父类2 ...):
    pass

如果一个类没有继承任何类，则默认继承object
Python支持多继承
定义子类时，必须在其构造函数中调用父类的构造函数
super().__init__(self,传入其他形参)，也可以用 父类名.__init__(self,传入其他形参)
super()是直接调用父类的一个方法
"""


# 定义父类
class Person(object):  # object可以省略，如果一个类没有继承任何类，则默认继承object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


# 定义子类
class Student(Person):
    def __init__(self, name, age, stu_no):  # stu_no是学号
        super().__init__(name, age)  # super()可以调用父类的属性，这个格式适用于多继承时调用多个父类实例属性的情况
        # 也可以改用
        # Person.__init__(name, age)
        self.stu_no = stu_no


# 定义第二个子类
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


# 创建对象
stu = Student("张三", 20, 1001)
teacher = Teacher("李四", 34, 10)

stu.info()
teacher.info()


# 多继承

class A:
    pass

class B:
    pass

class C(A, B):
    pass
