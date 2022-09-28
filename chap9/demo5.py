# 开发人员：leo
# 开发时间：2022/9/27 15:15

# 字符串的劈分操作

"""
.split()
从左边开始劈分，默认分隔符是用空格字符串，返回值是一个列表
参数sep指定劈分符，不指定默认是空格  eg： sep='|'分隔符是竖线
参数maxsplit指定最大劈分次数，达到最大次数后，剩余的子串会单独作为一部分

.rsplit()
从右边开始劈分，其余同上
"""

s = 'hello world python'
lst = s.split()
print(lst)

s1= 'hello|world|Python'
print(s1.split(sep = '|'))
print(s1.split(sep = '|', maxsplit=1))

print("——————————————")

print(s.rsplit())
print(s1.rsplit(sep = '|'))
print(s1.rsplit(sep = '|', maxsplit=1))