# 开发人员：leo
# 开发时间：2022/10/24 14:33

# os.path模块操作目录相关函数

"""
在Python中，用'/'表示相对路径，'\'表示绝对路径，例如'../chap1'是相对路径，是'D:\\user'绝对路径
以下函数的参数都是str类型，需要用引号''

abspath(path)       用于获取文件或目录的绝对路径，包含文件/目录名
exists(path)        用于判断文件或者目录是否存在，存在返回True，不存在返回False
join(path,name)     将目录与目录或文件名拼接起来，返回一个新的路径
splitext()          分离文件名和扩展名
split(path)         分离路径与文件名
basename(path)      从一个目录中提取文件名，'D:\\pkg\geek.exe'返回geek.exe
dirname(path)       从一个路径中提取文件路径，不包括文件名，'D:\\pkg\geek.exe'返回D:\pkg
isdir(path)         用于判断是否为路径

"""

import os, os.path
print(os.path.abspath('demo10.py'))
print(os.path.exists('demo10.py'), os.path.exists('demo55.py'))
print(os.path.join('D:\pkg', 'geek.exe'))
exe1 = os.path.join('D:\pkg', 'geek.exe')
# os.system(exe)
print(os.path.splitext('demo8.py'))
print(os.path.split('D:\\pkg\geek.exe'))
print(os.path.basename('E:\home\myphd\learnPython\chap15\demo10.py'))
print(os.path.dirname('E:\home\myphd\learnPython\chap15\demo10.py'))
print(os.path.dirname('D:\\pkg\geek.exe'))
print(os.path.isdir('E:\home\myphd\learnPython\chap15\demo10.py'))