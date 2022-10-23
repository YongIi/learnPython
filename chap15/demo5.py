# 开发人员：leo
# 开发时间：2022/10/23 21:27

# 文件对象的常用方法

"""
read([size])            从文件中读取size个字节或字符的内容返回。若省略size，则一次读取文件所有内容，从头到尾
readline()              从文本文件中读取一行内容
readlines()             把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回
write(str)              将字符串str内容写入文件
writelines(s_list)      将字符串列表s_list写入文本文件，不添加换行符
seek(offset[,whence])   把文件指针移动到新的位置，offset表示相对于whence的位置
                        offset：为正往结束方向移动，为负王开始方向移动
                        whence不同的值代表不同的意义
                        0：从文件头开始计算（默认值）
                        1：从当前位置开始计算
                        2：从文件尾开始计算
tell()                  返回文件指针的当前位置
flush()                 把缓冲区的内容写入文件，但不关闭文件。Python中数据是先写到缓冲区，再写入磁盘的。作用是刷新缓冲区，清空缓冲区。
close()                 把缓冲区的内容写入文件，同时关闭文件，释放调用文件对象的相关系统资源。注意close()有一个写入操作。

"""

file = open('a.txt', 'r')
print(file.read())
file.close()

file = open('a.txt', 'r')
print(file.readline())
file.close()

file = open('a.txt', 'r')
print(file.readlines())
file.close()

file = open('c.txt', 'w')
file.write('hello')
file.close()

file = open('d.txt', 'w')
lst = ['java', '\n', 'go', '\t', 'Python']
file.writelines(lst)
file.close()

file = open('a.txt', 'r')
file.seek(2)  #  seek(1)会报错，因为一个中文占2个字符
print(file.tell())  # 读取前文件指针位置
print(file.read())  # 读取文件
print(file.tell())  # 读取后文件指针位置
file.close()
