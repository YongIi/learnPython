# 开发人员：leo
# 开发时间：2022/9/7 14:56

# 字典的创建
"""
1、使用花括号
scores = {"张三": 100, "李四": 98}

2、使用内置函数dict()，采用赋值的形式，等号左侧是键key，等号右侧是值value，不同元素用逗号隔开

dict(name = 'jack', age = 20)

"""

scores = {"张三": 100, "李四": 98}
print(scores, type(scores))

stud = dict(name="jack", age=28)  # name和age是什么数据类型的？键都是字符串！？ 且定义字典时，不带引号的键只能在dict()中，不能用在{}定义时
print(stud, type(stud))

# 空字典
d = {}
print(d)

