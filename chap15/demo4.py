# 开发人员：leo
# 开发时间：2022/10/23 20:53

# 常用的文件打开模型

"""
file = open(filename [, mode, encoding])
指定mode的值

文件的类型
按文件中数据的组织形式，文件分为以下两大类：
a, 文本文件：存储的是普通“字符”文本，默认为unicode字符集，可以使用记事本程序打开
b, 二进制文件：把数据内容用“字节”进行存储，无法用记事本打开，必须使用专用的软件打开。举例：mp3音频文件，jpg图片，doc文档

打开模式
r       以只读模式打开文件，文件的指针将会放在文件的开头。？？？？？什么是文件的指针
w       以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头。覆盖写入
a       以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追究内容，文件指针在原文件末尾  # append
b       以二进制方式打开文件，不能单独使用，需要与其它模式一起使用，rb或者wb。一般是处理二进制文件时采用，例如复制图片
+       以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+

"""

file = open('b.txt', 'w')  # 覆盖写入
file.write("hello world")
file.close()  # 关闭调用的操作系统资源

file = open('b.txt', 'a')  # 追加
file.write("hello python")
file.close()  # 关闭调用的操作系统资源

src_file = open('convection.png', "rb")
target_file = open('copiedConvection.png', 'wb')
target_file.write(src_file.read())  # 对二进制文件边读边写，即复制
src_file.close()
target_file.close()


