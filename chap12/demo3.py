# 开发人员：leo
# 开发时间：2022/10/11 17:41

# 类的创建

"""
1、创建语法
clss 类名:
    pass

2、类的组成
a. 类属性
b. 实例方法
c. 静态方法
d. 类方法

"""


class Student:  # Student为类名，类名可以由一个或者多个单词组成，每个单词的首字母大写，其余小写（就是驼峰写法）
    pass


# Python中一切皆对象，那类名Student是对象吗？内存有对它开辟空间吗？  是对象，开辟了空间，有类型有值
print(id(Student))  # 查看类名的地址
print(type(Student))  # <class 'type'>  # 查看类名的类型
print(Student)  # <class '__main__.Student'>  # 查看类名的内容


