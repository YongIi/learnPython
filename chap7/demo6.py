# 开发人员：leo
# 开发时间：2022/9/12 13:44

# 字典的特点
"""
1. 字典中所有元素都是key-value对，key不允许重复，但value可以重复
2. 字典中的元素是无序的
3. 字典中的key必须是不可变对象，目前学的不可变对象有整数和字符串
4. 字典也可以根据需要动态的伸缩（增删改）
5. 字典会浪费较大的内存，是一种使用空间换时间的数据结构。因为存储位置取决于hash函数计算出来的位置，中间会浪费很多空余的空间，但查找速度很快

"""

d = {"name": "张三", "name": "李四"}  # key不允许重复，"name"对应的值被覆盖了
print(d)

d = {"name": "张三", "nikename": "李四"}  # value允许重复
print(d)

# d = {name: "张三"}  # 错误，定义字典时，不带引号的键只能在dict()中，不能用在{}定义时

lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

# d = {lst: 100}  # 列表不可以作为键