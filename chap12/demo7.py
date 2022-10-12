# 开发人员：leo
# 开发时间：2022/10/12 16:29

# 动态绑定属性和方法

"""
Python是动态语言，在创建对象后，可以动态地绑定属性和方法
即：在创建对象后，继续为该对象添加属性和方法

以下面的代码为例，一个Student类可以创建N多个Student类的对象，每个实体对象的实例属性（name和age）都是各自对象的，且不同
"""


# 创建类
class Student:
    def __init__(self, name, age):  # 初始化方法，构造函数
        self.name = name  # 局部变量赋值给实例变量
        self.age = age
    def eat(self):
        print(self.name+"正在吃饭")

# 创建对象
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)

print("---在code运行过程中，Python由于动态编译已经为stu1和stu2开辟内存空间了---")
print(id(stu1))
print(id(stu2))

print("---现在想为对象stu2添加新的实例属性（性别）---")
stu2.gender = "女"  # 动态绑定性别属性，仅为该对象添加新的属性
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print("---对象调用方法的一般情况：调用公共方法---")
stu1.eat()
stu2.eat()

print("---为stu2单独添加一个show函数（）---")
def show():
    print("定义在类外的，称为函数；定义在类内的，称为方法")

stu2.show=show  # 动态地绑定方法（函数），不需要加小括号()，仅为该对象添加新的方法
stu2.show()  # 调用时还是需要添加小括号()
