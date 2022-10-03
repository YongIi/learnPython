# 开发人员：leo
# 开发时间：2022/10/3 19:37

"""
需求c和d只能采用关键字实参传递
"""

def fun6(a, b, *, c, d):  #  *后只能采用关键字实参传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

# fun6(1, 2, 3, 4)  # 位置实参传递
fun6(a=1, b=2, c=3, d=4)  # 关键字实参传递
fun6(1, 2, c=3, d=4)  # 前两个参数采用位置实参传递，后两个采用关键字实参传递

'''
函数定义时的形参顺序问题
'''

def fun1(a,b,*,c,d,**args):
    pass

def fun2(*args1, **args2):
    pass

def fun3(a,b=10,*args1,**args2):
    pass