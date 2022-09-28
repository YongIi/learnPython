# 开发人员：leo
# 开发时间：2022/9/27 15:28

# 判断字符串

"""
.isidentifier() 判断字符串是否是合法的标识符（标识符由字母、数字和下划线组成，还包括汉字字符串，汉字字符串被视为字母）
.isspace()  判断字符串是否全部由空白字符组成（空格、回车、换行、水平制表符）
.isalpha()  判断是否全部由字母组成，还包括汉字字符串，汉字字符串被视为字母
.isdecimal()  判断是否全部由十进制的数字组成，小数不是十进制数字
.isnumeric()  判断是否全部由数字组成
.isalnum()  判断是否全部由字母和数字组成


"""

s = 'hello, python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', "张三".isidentifier())  # 标识符由字母、数字和下划线组成，还包括汉字字符串，汉字字符串被视为字母
print('4.', " ".isspace())
print('5.', '\t'.isspace())
print('6.', 'abc'.isalpha())
print('7.', "张三".isalpha())  # True 汉字字符串被视为字母
print('8.', "张三1".isalpha())
print('9.', "123".isdecimal())
print('10.', "123四".isdecimal())
print('11.',"3.14".isdecimal()) # False, 小数不是十进制数字
print('12.', "3.14".isnumeric())
print('13.', "123四五ⅠⅡⅢ".isnumeric())  # True  汉字数字，罗马数字都属于numeric
print("14.", "123Ⅰas".isalnum())
print("15.", "张三123".isalnum())
print("16.", "abc!".isalnum())