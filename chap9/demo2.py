# 开发人员：leo
# 开发时间：2022/9/25 21:41

# 字符串的常用操作

"""
字符串可以看作是关于字符的列表

1、查找
正向索引从0开始
逆向索引从-1开始

.index()  查找子串substr第一次出现的位置，如果找不到抛出ValueError异常
.rindex   查找子串substr最后一次出现的位置，如果找不到抛出ValueError
.find()   查找子串substr第一次出现的位置，如果找不到返回-1     <--建议使用
.rfind()  查找子串substr最后一次出现的位置，如果找不到返回-1   <--建议使用

"""

s = 'hello,hello'

print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

#print(s.index('k'))  # ValueError: substring not found
print(s.find('k'))