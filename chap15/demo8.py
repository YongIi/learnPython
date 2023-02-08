# 开发人员：leo
# 开发时间：2022/10/24 13:53

# 目录操作

"""
os模块是与操作系统相关的一个模块

os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样

os模块与os.path模块用于对目录或文件进行操作

"""

import os

os.system('notepad.exe')  # 打开系统上的记事本
os.system('calc.exe') # 打开系统上的计算器

# 直接调用可执行文件
os.startfile("D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe")  # 打开QQ，其中两个反斜杠\\是因为路径带转义字符