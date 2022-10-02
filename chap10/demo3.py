# 开发人员：leo
# 开发时间：2022/10/2 16:49

# 函数的返回值

'''
函数返回多个值时，结果是元组

函数的返回值
1、如果函数没有返回值（函数执行完后，不需要给调用处提供数据），可以省略return不写
2、函数的返回值如果只有1个，直接返回原值，是列表就返回列表，是整数就返回整数
3、函数的返回值如果是多个，返回的结果是元组，元组的每个元素是return的内容

函数在定义时，是否需要返回值要视情况而定

'''

def fun(num):
    odd=[]
    even=[]
    for i in num:  # num必须是可迭代对象
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

print(fun([10,29,34,23,44,53,55]))  # ([29, 23, 53, 55], [10, 34, 44]) 函数返回多个值时，结果是元组，该例子中每个元组元素都是返回的列表

print(fun(range(5)))  # ([1, 3], [0, 2, 4])

def fun1():
    print("hello")
    # return

def fun2():
    return "hello"

def fun3():
    return "hello", "world"

fun1()
print(fun2())
print(fun3())