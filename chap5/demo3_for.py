# 开发人员：leo
# 开发时间：2022/9/4 19:16

# for in循环
# in 从（字符串、序列等）中依次取值、遍历
# for in遍历的对象必须是可迭代对象，例如字符串、整数序列

# for 自定义的变量 in 可迭代对象:
# 循环体
# 当循环体内不需要使用到自定义变量时，可以将自变量写为下划线_

for item in 'Python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5):  # 同时也代表循环5次
    print("人生苦短，我用Python")

'''
使用for循环计算1-100之间的偶数和
'''
sum = 0
for item in range(1, 101, 1):
    if item % 2 == 0:
        sum += item
print("1-100之间的偶数和为：", sum)
