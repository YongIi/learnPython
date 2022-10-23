# 开发人员：leo
# 开发时间：2022/10/23 15:52

# Python中常用的内置模块

"""
常用标准库
sys         与Python解释器及环境操作相关的标准库
time        提供与时间相关的各种函数
os          提供访问操作系统服务功能的标准库，常与文件操作有关
calender    提供与日期相关的各种函数
urllib      用于读取来自网上（服务器）的数据，一般用来网上爬虫
math        提供标准算术运算函数
decimal     用于进行精确控制运算精度、有效位数和四舍五入操作的十进制运算，解决浮点数精度不准确问题
logging     提供灵活的记录事件、错误、警告和调试信息等日志信息的功能

"""

import sys  # 可Ctrl点开，查看与Python解释器及环境操作相关的内容
print(sys.getsizeof(24))   # 获得对象所占内存的大小
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time  # 提供与时间相关的各种函数
print(time.time())  # 输出的是秒
print(time.localtime(time.time()))  # 将上面的秒转为当地日期

import math
print(math.pi)



