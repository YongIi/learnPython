# 开发人员：leo
# 开发时间：2022/10/7 17:42

# traceback模块

"""
使用traceback模块打印异常信息

一般用于将异常信息放在log日志文件中
"""

import traceback
try:
    print("--------")
    print(10/0)
except:
    traceback.print_exc()