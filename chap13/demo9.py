# 开发人员：leo
# 开发时间：2022/10/18 14:58

# __new__与__init__演示创建对象的过程

"""
创建对象时，会先调用__new__方法创建对象（同时指定对象的类型），再调用__init__方法初始化对象
"""

class Person(object):
    # 重写object类的__new__方法
    def __new__(cls, *args, **kwargs):  # cls参数指当前正在实例化的类，会把Person传入，后面两个参数代表所有单字符串和列表对象，也就是说新对象的取名没有限制
        print("__new__被调用执行了，cls的id值为{0}".format(id(cls)))  # 查看将要创建对象的类型，就是上面传入的cls，即Person
        obj = super().__new__(cls)  # object.__new__(cls) 是创建一个对象，其类型是cls
        print("创建对象的id为{0}".format(id(obj)))
        return obj  # 传给__init__方法的self，即将创建的对象赋值给__init__方法中的self

    def __init__(self, name, age):
        print("__init__被调用执行了，self的id值为{0}".format(id(self)))
        self.name = name
        self.age = age

print("object这个类对象的id为：{0}".format(id(object)))
print("Person这个类对象的id为：{0}".format(id(Person)))
print("--------我是分割线--------")

# 创建Person类的实例对象
# 创建对象时，会先调用__new__方法创建对象（同时指定对象的类型），再调用__init__方法初始化对象
p1 = Person("张三", 20)  # 先执行赋值符=右侧的代码，会先把类对象Person传给__new__方法中的cls，创建对象并指定对象的类型，再调用__init__方法
# 相对于
p = object.__new__(Person)  # 此时只是创建对象，指定类型为Person，再要通过Person.__init__(p, "张三", 20)初始化对象
Person.__init__(p, "张三", 20)
print(p.name, p.age)
print("p1是这个Person类的实例对象，其id是{0}".format(id(p1)))
