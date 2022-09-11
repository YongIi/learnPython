# 开发人员：leo
# 开发时间：2022/9/6 10:41

# 获取列表中的多个元素，切片操作
"""
语法格式:
列表名[start: stop: step]

1、切片的结果：原列表片段的拷贝，是一个新的列表对象
2、切片的范围：[start,stop)   左闭右开，不包括stop
3、step默认为1，简写为[start, stop]
4、setp为正数
    [:stop:step] 从第一个元素到stop个元素，因为第一个元素的index是0
    [start::step] 从start到最后一个元素
5、step为负数，从start倒着往前计算切片，逆序同样不包括最后一个stop
    [:stop:step] 从最后一个元素到倒数第stop个元素
    [start::step] 从倒数第start个元素到第一个元素
"""

lst=[1,2,3,4,5,6,7,8]
print(lst[1:6:1])

lst2 = lst[1:6]  # 切片的结果：原列表片段的拷贝，是一个新的列表对象
print("原列表id：", id(lst))
print("新列表id：", id(lst2))

print(lst[1:6:2])  # [2, 4, 6]
print(lst[:6:2])  # [1, 3, 5]
print(lst[1::2])

print("---步长为负数---")
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])  # [7, 5, 3]  逆序同样不包括最后一个stop，故不考虑index为0的元素