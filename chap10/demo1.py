# 开发人员：leo
# 开发时间：2022/10/2 13:58

# 函数

'''
函数不调用就不会使用，函数运行完后其内的变量会销毁

函数就是执行特定任务、完成特定功能的一段代码

功能：
复用代码
隐藏实现细节
提高可维护性
提高可读性便于调试

创建：
def 函数名([输入参数]):
    函数体
    [return xxx]
'''

def calc(a,b):  # a和b是占位符，是形参，在函数的定义中
    c=a+b
    # print(a)
    return c

result = calc(10, 20)  # 10和20是实参，在函数的调用中
print(result)

"""
函数的传参
1、位置传参   按顺序传参
2、关键字传参  按=的关键字传参
定义时：
def calc(a, b):
调用时：
calc(b = 20, a = 10)
"""

print(calc(b = 5, a = 6))