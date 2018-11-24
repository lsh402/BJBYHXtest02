import time
import unittest
from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.yhd.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    # def test_login_001(self):
    #     # 点击登录
    #     self.driver.find_element_by_partial_link_text("登录").click()
    #     # 输入用户名
    #     self.driver.find_element_by_id("un").send_keys("hitheima")
    #     # 输入密码
    #     self.driver.find_element_by_id("pwd").send_keys("hitheima123000")
    #     # 点击登录
    #     self.driver.find_element_by_id("login_button").click()
    #
    #     # 断言
    #     assert "hitheima" == self.driver.find_element_by_class_name("hd_login_name").text

    # def test_login_002(self):
    #     # 点击登录
    #     self.driver.find_element_by_partial_link_text("登录").click()
    #     # 输入用户名
    #     self.driver.find_element_by_id("un").send_keys("hitheima")
    #     # 输入密码
    #     self.driver.find_element_by_id("pwd").send_keys("hitheima123000123")
    #     # 点击登录
    #     self.driver.find_element_by_id("login_button").click()
    #
    #     time.sleep(3)
    #
    #     # 断言
    #     assert "账号和密码不匹配，请重新输入" == self.driver.find_element_by_id("error_tips").text