# 开发人员：leo
# 开发时间：2022/7/11 16:05

# Python中一切都是“对象”
# Python中所有的变量都是指针，指向一个对象
# Python对指针做了良好封装，一切都是“对象”，一切对象都有一个“变量”指向它。这个“变量”就是“指针”。

name = "玛丽亚"  # 变量名是name，其内存保存的是对象“玛丽亚”的地址，指向对象“玛丽亚”
print(name)
name = "楚留冰"  # 变量名指向新的对象“楚留冰”，原来的对象“玛丽亚”会成为内存垃圾被系统回收
print(name)
