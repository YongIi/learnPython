# 开发人员：leo
# 开发时间：2022/7/8 17:08

# 可以输出数字、字符串、表达式
print(520)
print('hello world')
print("hello world")  # 双引号内可以用到转义字符\'
print(3 + 4)

# 将数据输出到文件当中，用open指定路径和打开方式，file=进行写入
fp = open('/chap1/test.txt', 'a+')  # a+代表读写模式进行追加，没有则创建
print('hello world', file=fp)
fp.close()

# 不换行输出
print('hello', 'world', 'python')
