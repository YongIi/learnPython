# 开发人员：leo
# 开发时间：2022/7/11 22:03
a = 3.1415926
print(a, type(a))

# 在python中浮点数存储不精确，使用浮点数计算时可能会出现小数位数不确定的情况
print(1.1 + 2.2)  # 计算结果为3.3000000000000003，这种情况也是个别情况
# 需要导入decimal模块进行矫形
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
