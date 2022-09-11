# 开发人员：leo
# 开发时间：2022/9/6 14:58

# 列表元素的增加操作
"""
append()    在列表的末尾添加一个元素，append是常用操作
extend()    在列表的末尾添加至少一个元素
insert()    在列表的任意位置添加一个元素
切片         在列表的任意位置添加至少一个元素，但会切掉后面的元素
"""

lst = [10, 20, 30]
print("添加元素之前：", lst, id(lst))
lst.append(40)
print("添加元素之后：", lst, id(lst))

lst2 = ["hello", "world"]
lst.append(lst2)  # 会将lst2作为一个元素放在lst的末尾，存放的是一个list对象
print(lst)

lst.extend(lst2)  # 在列表的末尾一次性添加多个元素
print(lst)

lst.extend("good")
print(lst)

lst.insert(2, "bad")  # 在指定的index位置添加一个元素，其他元素往后面排
print(lst)

# 用切片法在任意位置添加N多个元素
lst3 = [True, False, "hello"]
lst[1:] = lst3  # 对于
# lst，从index=1的位置开始替换为lst3
print(lst)