# 开发人员：leo
# 开发时间：2022/9/4 16:44

# while循环
# for in循环

# 四步循环法
## 初始变量
## 条件判断
## 循环体（执行体）
## 改变变量
# 初始化的变量、条件判断的变量、改变的变量为同一个


a = 1
while a < 10:
    print(a)
    a += 1

'''
累加0-4
'''
a = 0
sum = 0
while a <= 4:
    sum += a
    a += 1

print("和为：", sum)

'''
计算1-100之间的偶数和
'''
a = 1
sum = 0
while a <= 100:
    if a % 2 == 0:  # a是偶数就求和，该行也可以改写为   if not bool(a%2)
        sum += a
    a += 1
print("1-100之间的偶数和为：", sum)