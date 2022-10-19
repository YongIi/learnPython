# 开发人员：leo
# 开发时间：2022/10/19 11:26

# 类的浅拷贝与深拷贝

"""
(1)变量的赋值操作
cpu2 = cpu1
只是形成两个变量，实际上还是指向同一个对象

(2)浅拷贝
computer2 = copy.copy(computer)
Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此原对象和拷贝对象都会引用同一个子对象

(3)深拷贝
computer3 = copy.deepcopy(computer)
使用copy模板的deepcopy函数，递归拷贝对象中包含的子对象。原对象和拷贝对象所有的子对象也不相同

"""

# 变量的赋值操作

class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

# (1)变量的赋值操作
# """变量的赋值拷贝时，是同一个对象，由两个不同的变量指向同一个对象"""
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)  # 两者有相同的地址

# (2)类的浅拷贝
print("------------浅拷贝---------------")
disk = Disk()  # 创建一个Disk类对象
computer = Computer(cpu1, disk)  # 创建一个computer类对象
# 浅拷贝
import copy
computer2 = copy.copy(computer)  # 浅拷贝时会创建一个新的对象，但新的对象和原对象共用子对象
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# (3)类的深拷贝
print("------------深拷贝---------------")
computer3 = copy.deepcopy(computer)  # 深拷贝时也会创建一个新的对象，且新的对象会把原对象的子对象也拷贝一份
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)