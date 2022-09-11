# 开发人员：leo
# 开发时间：2022/7/11 22:25
# 字符串可以用单引号'' 双引号"" 三引号''' '''或""" """来定义
# 单/双引号只能在一行显示，三引号可以在连续的多行显示，回车也会被三引号收入

str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
str3 = '''人生苦短，
我用Python'''
str4 = """人生苦短，
我用Python"""

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))