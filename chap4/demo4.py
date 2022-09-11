# 开发人员：leo
# 开发时间：2022/9/3 16:51

# 嵌套if
"""
会员 消费>=200 8折
    消费>=100 9折
非会员 消费>=200 9.5折
"""

answer = input("您是会员吗？输入y或n\n")
money = float(input("请输入您的购物金额：\n"))

# 判断会员
if answer == "y":  # 会员
    print("会员")
    if money >= 200:
        print("打8折，付款金额为：", 0.8 * money)
    elif money >= 100:
        print("打9折，付款金额为：", 0.9 * money)
    else:
        print("不打折，付款金额为：", money)
else:  # 非会员
    print("非会员")
    if money >= 200:
        print("打9.5折，付款金额为：", 0.95 * money)
    else:
        print("不打折，付款金额为：", money)
