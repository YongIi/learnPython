# 开发人员：leo
# 开发时间：2022/10/24 14:07

# os模块操作目录相关函数

"""
getcwd()                        返回当前的工作目录
listdir(path)                   返回指定路径下的文件和目录信息
mkdir(path[, mode])             创建目录
makedirs(path1/path2[, mode])   创建多级目录
rmdir(path)                     删除目录
removedirs(path1/path2...)      删除多级目录
chdir(path)                     将path设置为当前工作目录

以上参数都是str类型，需要加引号''

"""

import os
print(os.getcwd())
print(os.listdir('../chap15'))
os.mkdir('newdir')
os.makedirs('A/B/C')
os.rmdir('newdir')
os.removedirs('A/B/C')
os.chdir('../')
print(os.getcwd())
os.chdir('./chap15')
print(os.getcwd())