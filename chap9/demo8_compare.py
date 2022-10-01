# 开发人员：leo
# 开发时间：2022/10/1 20:24

# 字符串的比较操作

"""
运算符：
>  >=  <  <=  ==  !=

比较规则：首先比较第一个字符，若相等则比较第二个字符，依次比较下去，直到两个字符串中的字符不相等，其后所有后续字符不再比较

比较原理：字符串进行比较时，比较的是ordinal value（序数值），该值可以用内置函数ord()得到。相对应的，根据序数值可以用内置函数chr()得到对应的字符串
ordinal value（序数值）是Unicode码，兼容ASCII码，兼容汉字
"""

print('apple' > 'app')  # True 因为apple比app长
print('apple' > "banana")  # False, 比较第一个字母时就不相等，会直接根据第一个字母的ordinal value比较大小
print(ord('a'), ord('b'))  # 97 < 98 故上一句代码是False
print(chr(97), chr(98))

print(ord("李"))
print(chr(26446))

"""
==与is的区别

==比较的是ordinal value是否相等
is比较的是id是否相等
"""

a=b='Python'
c='Python'
print(a==b)  # True
print(b==c)  # True
print(a is b)  # True
print(a is c)  # True
print(id(a))
print(id(b))
print(id(c))