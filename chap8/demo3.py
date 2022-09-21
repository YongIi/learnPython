# 开发人员：leo
# 开发时间：2022/9/21 11:16

# 本质是元组存储的元素地址不可改变，则不可变元素不能修改，可变元素（例如列表）也不能修改，但其内的数据可以修改

# 为什么要将元组设计成不可变序列
"""
在创建不可变序列对象之后，对象内部的所有数据就不能再修改了，避免修改数据导致的错误，方便多任务同时访问
在多任务环境下，同时操作对象时不需要加锁？加锁就是某个任务访问这个对象时会加锁，这样其他任务就无法访问这个对象
因此，在程序中尽量使用不可变序列
"""

"""
注意事项：
元组是不可以修改元素的，但可变元素（列表）的数据可以修改
本质是元组存储的元素地址不可改变，则不可变元素不能修改，可变元素（例如列表）也不能修改，但其内的数据可以修改

元组中存储的是对象的引用
a.如果元组中某位置的对象本身是不可变对象，则该位置不能再引用其他对象，eg:t=(10,[20,30],9)  不允许t[0]=300 不允许t[1]=60
b.如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以变 eg: t[1].append(100) t[1]依旧是原列表
"""

t=(10,[20,30],9)
print(t, type(t))
print(t[0], type(t[0]),id(t[0]))
print(t[1], type(t[1]),id(t[1]))
print(t[2], type(t[2]),id(t[2]))

# 尝试将t[1]修改为100
# t[1] = 100  # 元组是不允许修改元素的

t[1].append(100)  # 由于t[1]是列表，是可变序列，所以可以再列表中添加元素，而列表的内存地址不变
print(t[1], type(t[1]),id(t[1]))