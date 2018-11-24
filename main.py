import time
import unittest
from base.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':

    # 获取所有的要运行的方法（scripts文件夹下的所有继承TestCase的test开头的方法）
    suite = unittest.defaultTestLoader.discover("./scripts", "test_*.py")
    # 运行！

    # unittest.TextTestRunner().run(suite)


    # 关于读写文件
    # f = open("xxx.txt", "w")
    # f.write("xxxx")
    # f.close()
    #
    # with open("xxx.txt", "w") as f:
    #     f.write("xxxx")



    # f = open("./report.html", "wb")
    #
    # HTMLTestRunner(f, 2, "这是一号店的登录", "mac os 10.13").run(suite)
    #
    # f.close()

    time_name = time.strftime("%y-%m-%d_%H_%M_%S")
    file_name = "./report/report-%s.html" % time_name
    with open(file_name, "wb") as f:
        HTMLTestRunner(f, 2, "这是一号店的登录", "mac os 10.13").run(suite)


