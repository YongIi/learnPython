# 开发人员：leo
# 开发时间：2022/9/23 20:58

# 集合的数学操作
"""
1、交集
.intersection()
或者使用 s1 & s2

2、并集
.union()
或者使用 s1 | s2

3、差集
.difference()
或者使用 s1 - s2

4、对称差集，挖掉共同的
.symmetric_difference()
或者使用 ^
"""

# 交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)

# 并集
print(s1.union(s2))
print(s1 | s2)

# 差集
print(s2.difference(s1))
print(s2 - s1)
print(s1.difference(s2))
print(s1 - s2)
print(s1, s2)  # 操作后原集合没有变化

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)