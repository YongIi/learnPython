# 开发人员：leo
# 开发时间：2022/9/25 21:52

# 字符串的大小写转换

"""
以下所有转换都会产生新的对象，即使全部小写用了.lower字符串没发生改动也会产生新的对象，id会不一样
.upper()  所有字符都转成大写
.lower()  所有字符都转成小写
.swapcase()  所有小写转成大写，所有大写转成小写
.capitalize()  第一个字符转为大写，其余小写
.title()  把每个单词的第一个字符转成大写，每个单词其余字符转成小写

"""

s = "hello, python"
a = s.upper()
b = s.lower()

print(s, id(s))
print(b, id(b))  # 转换都会产生新的对象，即使全部小写用了.lower字符串没发生改动也会产生新的对象，id会不一样
print(b == s, b is s)


print(a, id(a))
print(a.lower(), id(a.lower()))

s2 = "hello, Python"
print(s2.swapcase())
print(s2.title())
