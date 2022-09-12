# 开发人员：leo
# 开发时间：2022/9/12 16:12

# 元组的创建方式

"""
方式1：
直接用小括号()
该方法甚至可以省略掉小括号()
当元组只有一个元素时，为了和赋值区分，只包含一个元素的元组需要使用逗号和小括号，不加逗号会被认为是本身的数据类型进行赋值

方式2：
使用内置函数tuple()  # tuple()内部要带上元组的小括号()





"""

t = ("Python", "hello", 90)
print(t, type(t))

t1 = "Python", "hello", 98  # 省略了小括号
print(t1, type(t1))

t11 = ("Python")  # 还是被理解为str了
print(t11, type(t11))

t111 = ("Python",)  # 如果元组中只有一个元素，逗号不能省略
print(t111, type(t111))

t2 = tuple(("Python", "hello", 90))
print(t2, type(t2))


# 空元组的创建方式
t = ()
t2 = tuple()

# 空列表的创建方式
lst = []
lst1 = list()  # 内置函数依旧用小括号

# 空字典的创建方式
d = {}
d2 = dict()  # 内置函数依旧用小括号

print("空元组：", t, t2)
print("空列表：", lst, lst1)
print("空字典：", d, d2)


