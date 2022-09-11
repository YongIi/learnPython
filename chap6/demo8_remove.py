# 开发人员：leo
# 开发时间：2022/9/6 21:38

# 删除列表中的元素

"""
remove()
一次删除一个元素，重复的元素只删除第一个，元素不存在是抛出ValueError

pop()
删除指定索引位置上的元素，指定索引不存在时抛出IndexError，不指定索引则删除最后一个元素

切片
一次至少删除一个元素

clear()
清空列表

del
删除列表
"""

lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)
print(lst)

# lst.remove(100)  # ValueError: list.remove(x): x not in list

# pop根据索引来删除元素
lst.pop(1)
print(lst)
lst.pop()  # pop()如果不指定参数，将删除列表中的最后一个元素
print(lst)

print("---切片操作至少删除一个元素，将产生一个新的列表对象---")  # 本质就是截取一个片段
new_lst2 = lst [1:3]
print(new_lst2)

"""
不产生新的列表对象，而是删除原列表中的内容
"""
lst[1:3] = []  # 本质是将lst索引为1到3（不包括3）的位置由空列表替代，达到：删除lst列表中1到3（不包括3）的元素
print(lst)

"""清空列表所有元素"""
lst.clear()
print(lst)

"""删除列表对象"""
del lst
# print(lst)  # NameError: name 'lst' is not defined.