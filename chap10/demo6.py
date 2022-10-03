# 开发人员：leo
# 开发时间：2022/10/3 17:31

def fun(a, b, c):  # 形式参数
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)  # 位置参数，按顺序传参
lst = [11, 22, 33]
# fun(lst)  # 会报错，因为会把lst传给a，而b和c并没有传参
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入

print("------------------")
fun(a=100, c=300, b=200)  # 关键字传参

dic = {'a': 111, 'b': 222, 'c': 333}
# fun(dic)  # # 会报错，因为会把lst传给a，而b和c并没有传参
fun(**dic)  # 在函数调用时，将字典中的键值对都转换为关键字实参传入


def fun2(a, b=10):  # b是默认值形参
    print('a=', a)
    print('b=', b)


def fun3(*args):  # 个数可变的位置形参
    print(args)


def fun4(**args):  # 个数可变的关键字形参
    print(args)


fun3(1, 2, 3, 4)
fun4(a=11, b=22, c=33)


def fun5(a, b, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun5(1, 2, 3, 4)  # 位置实参传递
fun5(a=1, b=2, c=3, d=4)  # 关键字实参传递
fun5(1, 2, c=3, d=4)  # 前两个参数采用位置实参传递，后两个采用关键字实参传递


