# 开发人员：leo
# 开发时间：2022/10/7 13:57

# 斐波那契数列

"""
首两个数值是1，其后的数值是前两个数的和
1 1 2 3 5 8 13 21 34 ...

"""

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# 斐波那契数列第9位的数字
print(fib(9))

# 斐波那契数列前6位的数字
for i in range(1,7):
    print(fib(i))