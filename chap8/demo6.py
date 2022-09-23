# 开发人员：leo
# 开发时间：2022/9/23 20:17

# 集合的操作

"""
1、判断
in或not in

2、新增
add() 一次添加一个元素
update()  至少添加一个元素

3、删除
remove()  一次删除一个指定元素，如果指定元素不存在抛出KeyError
discard() 一次删除一个指定元素，如果指定元素不存在不抛出异常
pop()  一次删除任意一个元素，pop()不能添加参数
clear()  清空集合

"""

# 判断
s = {10, 20, 30, 405, 60}
print(0 not in s)  # True
print(20 in s)  # True

# 新增
s.add(80)
print(s)

s.update({200, 300, 400})
print(s)
s.update([1, 2])
s.update((3, 4))
print(s)

# 删除
s.remove(1)
print(s)
# s.remove(10000)  # 一次删除一个指定元素，如果指定元素不存在抛出KeyError
s.discard(2)
s.discard(10000)
print(s)
s.pop()
# s.pop(20)  # pop()不能添加参数
print(s)
s.clear()
print(s)