# 开发人员：leo
# 开发时间：2022/9/7 13:29

# 列表元素的排序

'''
1、调用sort()方法，列表中所有元素默认按照从小到大进行排序（升序），可以指定reverse=True进行降序 排序

2、调用内置函数sorted(),可以指定reverse = True进行降序排序，原列表不发生改变
内置函数就是直接可以拿来用的函数，不需要用.加载

'''

lst = [20, 40, 10, 98, 54]
print("---排序前的列表---")
print(lst, id(lst))
lst.sort()
print("---排序后的列表---")
print(lst, id(lst))

lst.sort(reverse=True)  # reverse=True 是降序排列，reverse=False是升序排列
print(lst)
lst.sort(reverse=False)
print(lst)

print("---使用内置函数sorted()对列表进行排序，将产生一个新的列表对象---")
lst = [20, 40, 10, 98, 54]
print("原列表：", lst, id(lst))
new_lst = sorted(lst)  # sorted()将原列表排序好，然后放进一个新列表里
print("新列表：", new_lst, id(new_lst))

desc_lst = sorted(lst, reverse=True)
print("降序排列的新列表：", desc_lst, id(desc_lst))

