# 开发人员：leo
# 开发时间：2022/10/1 19:55

# 字符串的替换和合并

"""
替换
.replace()
第一个参数指定哪些字符被替换，第二个参数指定用什么字符替换，第3个参数指定最大替换次数
返回替换后的字符串，替换前的字符串不发生变化

合并
.join()
将列表或元组中的字符串合并成一个字符串

"""
# 替换
s = 'hello, Python'
print(s.replace('Python', "Java"))
print(s)

s1 = 'hello, Python, Python, Python'
print(s1.replace('Python', 'Java', 2))
print(s1)

# 合并
lst = ["hello", "java", "Python"]
print("|".join(lst))  # 使用"|"去链接各个元素
print("".join(lst))  # 使用空去链接各个字符串

t = ("hello", "java", "Python")
print(''.join(t))

print("*".join('Pyhon'))  # P*y*h*o*n  可以把字符串理解成列表