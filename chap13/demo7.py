# 开发人员：leo
# 开发时间：2022/10/18 10:42

# 特殊方法和特殊属性

"""
特殊属性或特殊方法：两个下划线__开头，两个下划线__结束的属性或方法

特殊属性：
__dict__  # 获得类对象或实例对象所绑定的所有属性和方法的字典（即自己定义的属性和方法，以字典的形式给出）
输出时，属性为键，属性值为字典的值
# 创建C类的对象
x = C("jack", 20)  # x是C类型的实例对象
print(x.__dict__)  # 展示实例对象的属性字典，不包括类中公有的类属性和方法
print(C.__dict__)  # 展示类对象的所有类属性和方法，不包括方法中的实例属性

print(x.__class__) # <class '__main__.C'>  获得该对象x所属的类
print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)  展示多继承时，所有父类，以元组形式给出
print(C.__base__) # <class '__main__.A'> 多继承时，先继承谁（谁写在前面）就输出谁，是类的基类
print(C.__mro__)  # 多继承时的层次结果，先继承A，再继承B，还继承了object类
print(A.__subclasses__())  # [<class '__main__.C'>, <class '__main__.D'>]查看A类的所有子类，以列表形式给出

特殊方法：
__len__()  # 通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
__add__()  # 通过重写__add__()方法，可使自定义对象具有“+”功能
__new__()  # 用于创建对象
__init__() # 对创建的对象进行初始化

"""

print(dir(object))  # dir()函数可以查看对象所有的属性和方法

print("---分隔符---")

class A:
    pass

class B:
    pass

class C(A, B):
    haha = "haha"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("干饭...")

class D(A):
    pass

# 创建C类的对象
x = C("jack", 20)  # x是C类型的实例对象
print(x.__dict__)  # 展示实例对象的属性字典，不包括类中公有的类属性和方法
print(C.__dict__)  # 展示类对象的所有类属性和方法，不包括方法中的实例属性

print(x.__class__) # <class '__main__.C'>  获得该对象x所属的类
print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)  展示多继承时，所有父类，以元组形式给出
print(C.__base__) # <class '__main__.A'> 多继承时，先继承谁（谁写在前面）就输出谁，是类的基类
print(C.__mro__)  # 多继承时的层次结果，先继承A，再继承B，还继承了object类
print(A.__subclasses__())  # [<class '__main__.C'>, <class '__main__.D'>]查看A类的所有子类，以列表形式给出
