# 开发人员：leo
# 开发时间：2022/9/2 21:14

# 位运算，将数据转成二进制进行计算，将结果再以十进制展示
# & 按位与
# | 按位或
# << 左移运算符：高位溢出、低位补0，相当于乘以2
# >> 低位溢出、高位补0，相当于除以2

print(4 & 8)  # & 同为1时结果才为1
print(4 | 8)  # | 同为0时结果才为0
print(4 << 1)  # 4向左移动1位，4*（2**1）
print(4 >> 1)  # 4向右移动1位，4/（2**1） 整除
