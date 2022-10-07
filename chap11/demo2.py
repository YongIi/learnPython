# 开发人员：leo
# 开发时间：2022/10/7 14:36

"""
Bug的常见分类：
2、知识不熟练导致的错误，例如：
（1）索引越界问题IndexError
lst = [11,22,33,44]  # 列表的索引是从0开始的
print(lst[4])

（2）append()方法使用掌握不熟练
lst=[]
lst=append('A','B','C')  # lst.append() 每次只能添加一个元素
print(lst)

solution：
多练，熟悉IDE的报错功能
"""

lst = [11,22,33,44]  # 列表的索引是从0开始的
print(lst[3])

lst=[]
lst.append('A')
print(lst)