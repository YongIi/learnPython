# 开发人员：leo
# 开发时间：2022/9/5 17:13

# 列表的特点
"""
1、列表元素按顺序有序排列
2、索引映射唯一一个数据，正序索引从0开始，逆序索引从-1开始
3、列表可以存储重复数据
4、任意数据类型混存
5、根据需要动态分配和回收内存，不用担心列表的维度不够用

"""

lst=["hello", "world", 98, "hello"]  # lst是列表对象的名称，保存的是列表的地址id，而列表里面存储的是各个元素的地址id，指向各个元素

print(lst[0])  # 正序索引从0开始
print(lst[-1])  # 逆序索引从-1开始
print(lst[-4])