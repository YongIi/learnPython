# 开发人员：leo
# 开发时间：2022/10/18 14:19

# 特殊方法

"""
特殊方法：
__len__()  # 通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
__add__()  # 通过重写__add__()方法，可使自定义对象具有“+”功能
__new__()  # 用于创建对象
__init__() # 对创建的对象进行初始化
"""

a = 20
b = 100
c = a + b  # 代码底层是两个整数类型对象的相加操作，本质如下：
d = a.__add__(b)

print(c)
print(d)


# 通过重写__add__()方法，可使自定义对象具有“+”功能
class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  # 重写__add__()方法，类似C++中的运算符重载实现
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("张三")
stu2 = Student("李四")
print(stu1 + stu2)  # 实现两个对象的加法运算（因为在类中重写了__add__()方法）
print(stu1.__add__(stu2))  # 两个对象相加的本质

print("--------len()---------")

lst = [11, 22, 33, 44]
print(len(lst))  # 4 len()是内置函数，可以计算列表的长度，本质如下：
print(lst.__len__())
# 如果想输出一个对象的长度，就需要重写__len__()方法
print("---给自己的对象重写len()---")
print(len(stu2))  # 本质如下：
print(stu2.__len__())
