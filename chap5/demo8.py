# 开发人员：leo
# 开发时间：2022/9/5 15:57

# 嵌套循环
"""
输出一个3行4列的矩形
"""

for i in range(1, 4):  # 行数
    for j in range(1, 5):  # 列数
        print("*", end='\t')  # end='\t'表示打印后不换行，以\t结束
    print()  # 换行

"""
打印9×9的直角三角形
"""

for i in range(1, 10):  # 行数
    for j in range(1, 10):  # 列数
        if j <= i:
            print("*", end="\t")
    print()

# 减少循环，提高效率
for i in range(1, 10):  # 行数
    for j in range(1,i+1):
        print("*", end="\t")
    print()

"""
9×9乘法表
"""
for i in range(1, 10):  # 行数
    for j in range(1,i+1):
        print(i, "*", j, "=", i*j, end="\t")
    print()