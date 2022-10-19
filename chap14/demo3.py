# 开发人员：leo
# 开发时间：2022/10/19 16:06

"""
方法二：
from 模块名称 import 函数/变量/类
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
这样就不需要再使用.来调用了，可以直接使用
"""

from math import pi
from calc import div
print(pi)
print(div(6,3))