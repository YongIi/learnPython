# 开发人员：leo
# 开发时间：2022/8/10 22:02

# 比较运算符的结果是bool类型
# >,<,>=,<=,!=
# == 比较对象值value的大小
# is, is not  比较对象的id

a, b = 10, 20
print("a>b?", a > b)
print("a<b?", a < b)

a = 10
b = 10
print(a == b)  # True, a和b的值是相等的（或者说a和b指向对象的值是相等的）
print(a is b)  # True, a和b保存的地址id一样，指向的是同一个对象

# 以下代码暂时没学，后面会学
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # True，比较值
print(lst1 is lst2)  # False，比较地址id
print(id(lst1))
print(id(lst2))
print(lst1 is not lst2)
