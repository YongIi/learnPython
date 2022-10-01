# 开发人员：leo
# 开发时间：2022/10/1 21:50

# 字符串的编码转换

'''
字符串在不同电脑间传递字符串时，例如从主机传到显示屏
编码：将字符串转换成二进制数据（bytes）
解码：将bytes类型的数据转换成字符串类型
'''

s = '天涯共此时'

# 编码
print(s.encode(encoding='GBK'))  # 在GBK编码格式中一个中文占两个字节，encode()将字符串编码成二进制数据（字节类型的数据），encoding指定编码格式
print(s.encode(encoding='UTF-8'))  # 在UTF-8编码格式中一个汉字占3个字节

# 解码
# byte代表一个二进制数据，是上面字符串编码后的二进制数据
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte = s.encode(encoding='UTF-8')  # 编码
print(byte.decode(encoding='UTF-8'))  # 解码