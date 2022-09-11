# 开发人员：leo
# 开发时间：2022/7/8 17:55

# 转义字符
print('hello\nworld')  # \+转义功能的首字母  n对应newline的首字母
print('hello\tworld')
print("hello\rworld")  # \r是回车return，会覆盖前面的hello
print("hello\bworld")  # \b是退格

print("http:\\\\www.baidu.com")
print('老师说：”大家好“')
print('老师说：\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用——在字符串前面加上r或者R
print(r'hello\nworld')
# 注意事项，但最后一个字符不能是反斜杠\，但可以是两个反斜杠\\
# print(r'hello\nworld\')  #会提示缺少右引号'
print(r'hello\nworld\\')
