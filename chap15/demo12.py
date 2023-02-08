# 开发人员：leo
# 开发时间：2022/10/24 15:11

# 递归遍历所有文件，包括子文件夹底下的文件

import os

path = os.getcwd()
lst_files = os.walk(path)  # 迭代器对象，返回的是一个元组(路径，该路径下的目录名，该路径下的文件名)，递归遍历时包含当前目录
print(lst_files)
for dirpath, dirname, filename in lst_files:
    """
    print(dirpath)
    print(dirname)
    print(filename)
    print('----------')
    """
    for dir in dirname:
        print(os.path.join(dirpath, dir))  # 链接目录和子目录名
    print("-------------------------------------")
    for file in filename:
        print(os.path.join(dirpath, file))  # 链接目录和文件名
    print("---该目录完---")

