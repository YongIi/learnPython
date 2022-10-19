# 开发人员：leo
# 开发时间：2022/10/19 15:46

# 自定义模块

"""
(1)创建模块
新建一个.py文件，名称尽量不要与Python自带的标准模块名称相同

(2)导入模块
方法一：导入模块的所有
import 模块名称 [as 别名]
模块中的函数/变量/类 通过.来调用
可以用print(dir(模块名))查看可用的函数/变量等等

方法二：
from 模块名称 import 函数/变量/类
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
这样就不需要再使用.来调用了，可以直接使用

"""

import math  # 关于数学运算的模块
print(id(math))
print(type(math))
print(math)
print(math.pi)

print("--------")
print(dir(math))  # 查看math模块可用的函数/变量
print(math.pow(2,3))

print(math.ceil(9.0001))  # 大于它的最接近的整数
print(math.floor(9.9999))  # 小于它的最接近的整数


