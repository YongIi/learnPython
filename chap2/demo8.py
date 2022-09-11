# 开发人员：leo
# 开发时间：2022/7/11 23:17

# 数据类型转换
# 将不同数据类型的数据进行拼接的时候需要用到数据类型转换
# str() 将其他类型转化为字符串类型，也可以用引号转换
# int() 将其他类型转化为整型，浮点型转化为整型会抹零取整，文字类和小数类字符串不能转化为整型
# float() 将其他类型转化为浮点型，整数转化为浮点型，末尾加.0，文字类不能转化为浮点型

name = '张三'
age = 20

print(type(name), type(age))
print("我叫" + name + "，今年" + str(age) + "岁")  # “+”为连接符，但不能直接将字符串与整型数据进行链接，需要把整型数据转化为字符串

print("-----str()将其他类型转化为srt类型-----")
a = 10
b = 6.34
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

print("-----int()将其他类型转化为int类型-----")
s1 = "128"
f1 = 98.7
s2 = "45.67"
f2 = True
s3 = "hello"
print(type(s1), type(f1), type(s2), type(f2), type(s3))
print(int(s1), type(int(s1)))  # 将str转成int，字符串必须是整数数字串
print(int(f1), type(int(f1)))  # 将float转成int，只截取整数部分，舍弃小数部分
# print(int(s2), type(int(s2)))  # 将str转成int，报错，因为字符串不能是小数
print(int(f2), type(int(f2)))  # 将bool转成int，True为1，False为0
# print(int(s3), type(int(s3)))  # 报错，因为转化时字符串必须是数字串（整数）

print("-----float()将其他类型转化为float类型-----")
s1 = "128.98"
s2 = "45"
f2 = True
s3 = "hello"
i = 98
print(type(s1), type(s2), type(f2), type(s3), type(i))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(f2), type(float(f2)))
# print(float(s3), type(float(s3)))  # 字符串中的数据如果是非数字串，则不允许转换
print(float(i), type(float(i)))