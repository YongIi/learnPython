# 开发人员：leo
# 开发时间：2022/9/3 16:31

# 多分支结构
"""
从键盘录入一个整数成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于0或大于100 为非法数据
"""

score = int(input("请录入一个成绩：\n"))

if  score>=90 and score<=100:
    print("成绩：A")
elif score>=80 and score<=89:
    print("成绩：B")
elif score >= 70 and score <= 79:
    print("成绩：C")
elif score >= 60 and score <= 69:
    print("成绩：D")
elif score >= 0 and score <= 59:
    print("成绩：E")
else:
    print("输入的成绩不在合理范围内")