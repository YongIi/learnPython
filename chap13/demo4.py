# 开发人员：leo
# 开发时间：2022/10/16 13:57

# 方法重写

"""
如果子类对继承自父类的某个属性或方法（函数）不满意，可以在子类中对其（方法体，函数体内容）进行重新编写

子类重写后的方法中可以通过super().函数名() 调用父类中被重写的方法

"""


#  复制demo3的内容，进行方法重新

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
    def info(self):
        print(self.stu_no)  # 重写的内容
        super().info()  # 调用父类的函数


# 定义第二个子类
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear
    def info(self):
        print(self.name, self.age, self.teachofyear)


# 创建对象
stu = Student("张三", 20, 1001)
teacher = Teacher("李四", 34, 10)

stu.info()
teacher.info()