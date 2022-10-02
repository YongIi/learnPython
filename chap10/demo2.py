# 开发人员：leo
# 开发时间：2022/10/2 16:14

# 函数调用的参数传递内存分析

"""
传递可变对象和不可变对象传参的内存变化

函数调用过程中，进行参数传递时
如果传递的是不可变对象，在函数体内的修改不会影响实参的值  形参arg1修改为100，不会影响实参n1的值
如果传递的是可变对象，在函数体内的修改会影响到实参的值  形参arg2的修改，append(10)，会影响实参n2的值

只看函数的定义方便看传入的实参是什么类型
"""

def fun(arg1, arg2):
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1 = ', arg1)
    print('arg2 = ', arg2)
    # return  # 没有返回值时可以不写return，或者只写return不带返回值

n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
print('——————————————')
fun(n1, n2)  # 位置传参
print(n1)
print(n2)
