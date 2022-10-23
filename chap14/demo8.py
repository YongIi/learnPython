# 开发人员：leo
# 开发时间：2022/10/23 16:14

# 第三方模块的安装及使用

"""
安装：
在终端中输入以下cmd
pip install 模块名
如果提示没有pip，可以先运行以下命令安装pip
python -m pip install -U pip
在终端用pip下载的包库并不能直接被pyCharm使用，需要在setting中设置，找到解释器点+号搜索相关的包库再安装，
或者直接点击波浪线进行安装，此时要注意是安装正确的包（可能因为很多包有同名模块，可能推荐的包并不是真正想安装的包）

使用：
import 模块名


"""
import time

import schedule  # 在终端用pip下载的schedule包库并不能直接被pyCharm使用，需要在setting中设置，或者直接点击波浪线进行安装


def job():
    print("哈哈哈哈 ------------")


schedule.every(3).seconds.do(job)  # 安排每3秒运行一次job函数
while True:
    schedule.run_pending()  # 执行schedule的安排
    time.sleep(1)  # 休眠1秒