# 开发人员：leo
# 开发时间：2022/9/5 15:14

# continue语句，用于结束当前循环，进入下一次循环，通常与分支结构if一起使用

'''
输出1-50之间所有5的倍数：和5的余数为0的数
'''

for item in range(1,51):
    if item%5 == 0:
        print(item)

print("----使用continue----")

for item in range(1,51):
    if item%5 != 0:
        continue
    print(item)