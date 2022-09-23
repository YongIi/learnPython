# 开发人员：leo
# 开发时间：2022/9/23 22:41

# 集合生成式
"""
元组是所学数据中唯一的不可变序列，所有没有元组生成式

将列表生成式中的[]改为{}即可
{i*i for i in range(1, 10)}

"""
# 列表生成式
lst = [i*i for i in range(1, 10)]
print(lst, type(lst))

# 集合生成式
s = {i*i for i in range(1, 10)}
print(s, type(s))