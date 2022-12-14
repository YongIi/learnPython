# 开发人员：leo
# 开发时间：2022/10/19 16:25

# 以主程序形式运行

"""
在每个模块的定义中都包括一个记录模块名称的变量__name__，程序可以检查该变量，以确定他们在哪个模块中执行
如果一个模块不是被导入到其他程序中执行，那么它可能在解释器的顶级模块中执行。顶级模块的__name__变量的值为__main__

理解：每个模块都由变量__name__记录名称，当以本文件开始执行时，该文件则作为解释器的顶级模块，顶级模块的__name__变量的值变为__main__

if __name__ = '__main__'
    pass

"""

import calc2
print(calc2.add(100,200))

"""
calc2.py文件中有一个语句print(add(10,20))
输出结果：
30
300
输出结果中，calc2中的输出语句也输出了，但不希望如此
"""