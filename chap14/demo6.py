# 开发人员：leo
# 开发时间：2022/10/23 15:18

# Python中的包

"""
包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下

作用：
代码规范
避免模块名称冲突（例如chap1和chap2中都有demo1）

包与目录的区别：
包含__init__.py文件的目录称为包
目录里通常不包含__init__.py文件

包的导入：
import 包名.模块名

导入带包的模块时注意事项：
使用import方式进行导入时，只能跟包名或是模块名
import 包名
import 模块名
使用from...import方式可以导入包名、模块、函数、变量（多了函数和变量）
from package1.module_B import b


"""

import package1.module_A as A
from package1.module_B import b

print(A.a)
print(b)