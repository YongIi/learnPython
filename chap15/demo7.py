# 开发人员：leo
# 开发时间：2022/10/24 11:06

# with语句（上下文管理器）

"""
python进行文件操作时建议采用with语句

with语句可以自动管理上下文资源，不论什么原因跳出with语句，都能确保文件正确的关闭，以此达到释放资源的目的

使用with语句就不用手动关闭系统资源了，离开with语句时会自动释放资源

with open('logo.png', 'rb') as src_file
with和as之间是上下文表达式，结果是一个上下文管理器（实例对象），由src_file指向它
上下文管理器：一个类对象，它实现了特殊方法：__enter__()和__exit__()，则称为该类对象遵守上下文管理器协议，其实例对象称为上下文管理器
上下文表达式创建上下文管理器时会创建一个运行时上下文，也就是会自动调用__enter__()方法，并将返回值（实例对象）复制给src_file，这是src_file指向它的原因
with下的缩进内容称为with的语句体，该语句体执行完后会自动跳出上下文管理器，并调用__exit__()方法。无论with语句体是否出现异常，最后都有再调用一下__exit__()方法
调用__exit__()方法会自动关闭资源。（有点像析构函数）
"""

with open('a.txt', 'r') as file:
    print(file.read())

# 自己写一个上下文管理器
class myContentMgr(object):  # 一个类对象，它实现了特殊方法：__enter__()和__exit__()，该类对象遵守上下文管理器协议
    def __enter__(self):
        print("enter方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行了")

    def show(self):
        print("show方法被调用执行了")

# 该类对象的实例对象称为上下文管理器

with myContentMgr() as file:  # 相当于file = myContentMgr()，赋值给file时会调用__enter__()方法
    file.show()
    # with下的缩进内容称为with的语句体，该语句体执行完后会自动跳出上下文管理器，并调用__exit__()方法。无论with语句体是否出现异常，最后都有再调用一下__exit__()方法

# 复制图片
with open('with语句.jpg', 'rb') as src_file:  # 原图片的上下文管理器
    with open('copiedWith语句.jpg', 'wb') as target_file:  # 目标图片的上下文管理器
        target_file.write(src_file.read())