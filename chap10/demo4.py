# 开发人员：leo
# 开发时间：2022/10/2 17:17

# 函数的参数定义（形参）

'''
函数定义时，给形参设置默认参数，只有与默认参数不符的时候才需要传递实参
'''


def fun(a, b=10):  # b称为默认值参数
    print(a, b)

fun(100)
fun(20,30)

def fun1(a, b=20, c=30):
    print(a, b, c)

fun1(1,2)

print()  # 选中后按住ctrl+b跳到源码
print('hello', end='\t')  # 查看源码发现print()函数的end参数默认是'\n'
print('world')