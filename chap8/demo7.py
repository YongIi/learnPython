# 开发人员：leo
# 开发时间：2022/9/23 20:39

# 集合间的关系

"""
1、是否相等
==  !=

2、一个集合是否是另一个集合的子集
调用函数.issubset()进行判断
B是A的子集

3、一个集合是否是另一个集合的超集
调用函数.issuperset()进行判断

4、两个集合是否没有交集
调用函数.isdisjoint()


"""

s = {10, 20, 30, 40}
s2 = {30, 40, 20 ,10}
print(s == s2)
print(s != s2)

s3 = {10, 20}
s4 = {10, 60}
s5 = {10, 20, 30, 40, 50, 60}
print(s3.issubset(s))
print(s4.issubset(s))
print(s5.issuperset(s))

s6 = {100, 200}
print(s.isdisjoint(s4))
print(s.isdisjoint(s6))
