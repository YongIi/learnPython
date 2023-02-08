# 开发人员：leo
# 开发时间：2022/10/24 15:05

# 列出当前目录下的py文件

import os
path = os.getcwd()
lst = os.listdir(path)
print(lst)
for filename in lst:
    if filename.endswith('.py'):  # .endswith("abc")判断某字符串是否以abc结尾
        print(filename)
