# 开发人员：leo
# 开发时间：2022/9/2 22:30

# 单分支结构

money = 1000
s = int(input("请输入取款金额："))  # 取款金额
if money >= s:
    money -= s
    print("取款成功，余额为：", money)
