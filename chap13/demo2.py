# 开发人员：leo
# 开发时间：2022/10/15 15:07

# 面向对象的三大特征：封装、继承、多态

"""
面向对象的三大特征与语言本身是没有关系的，其他语言也有，只是一种编程思想

封装：提高程序的安全性
1、将数据（属性）和行为（方法、函数）包装到类对象中。在方法（函数）内部对属性进行操作，在类对象的外部调用方法。
这样，无需关心方法（函数）内部的具体实现细节，从而隔离了复杂度
2、在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个__下划线，（例如构造函数__init__）
但可以在类的内部使用，也可以在类的外部采用方法（函数）调用，甚至可以用dir(对象名)查看该变量名，直接用'_类名__变量名'调用
"""

class Student:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个下划线__
    def show(self):
        print(self.name, self.__age)  # 访问实例属性都需要加上self.***

stu = Student("张三", 20)
stu.show()  # 调用类对象内的函数访问带__的变量（实例属性）

# 在类的外部使用name与__age
print(stu.name)
# print(stu.__age)  # 带下划线__的实例属性不能在类外被访问

print(dir(stu))  # dir(对象名)函数查看该对象拥有哪些属性（变量）和方法（函数） 带__的变量为'_类名__变量名'，其可以被访问，eg:'_Student__age'
print(stu._Student__age)  # 在类外可以通过'对象名._类名__变量名'使用
# 那封装还有什么意义？在Python中需要靠程序员的自觉性，看见__的变量不能直接调用，但非要访问也可以，只是不建议

# 例2

class Student2:
    def __init__(self, age):
        self.set_age(age)
    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            self.__age = 0
    def get_age(self):
        return self.__age

stu2 = Student2(150)
stu3 = Student2(50)
print(stu2.get_age())
print(stu3.get_age())

