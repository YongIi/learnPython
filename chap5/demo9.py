# 开发人员：leo
# 开发时间：2022/9/5 16:23

# 二重循环中的break和continue只用于控制本层的循环

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j, end="\t")
    print()