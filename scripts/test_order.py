import time
import unittest
from selenium import webdriver


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.yhd.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_order_001(self):
        cookies_str = "[{'name': 'provinceId', 'value': '2', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1610010813}, {'name': 'cityId', 'value': '2817', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1610010813}, {'name': 'yhd_location', 'value': '2_2817_51973_0', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1610010813}, {'name': '__jdv', 'value': '259140492|direct|-|none|-|1540890814743', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1542186814}, {'name': 'msessionid', 'value': 'QR4GFNCD1A36YWV2XH167KDFSQ764DTQPRZS', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': None}, {'name': 'rURL', 'value': 'http%3A%2F%2Fwww.yhd.com%2F', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': None}, {'name': 'cid', 'value': 'NWlIMTUyNmJKMDkyN2tDOTE0OHZaMTE4MW5BNTMyMmJaMDUwM3FPNzkwNGtLNzE2', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 3688374467}, {'name': 'ut', 'value': '3RXMUDZ2U6ZBRJFKJ6DJRDFM1U21KKVQ1Q1AN6L90', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': True, 'expiry': None}, {'name': 'pin', 'value': '*yhd_pNEiDIx', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': None}, {'name': 'seus', 'value': '4LS9I0176VB8Y2W47B39FH7', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': None}, {'name': 'uname', 'value': 'hitheima', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1571994827}, {'name': 'yihaodian_uid', 'value': '278455320', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1571994827}, {'name': 'JSESSIONID', 'value': 'CB4161B93C67114B1170C18ACB35FE2B.s1', 'path': '/', 'domain': 'www.yhd.com', 'secure': False, 'httpOnly': True, 'expiry': None}, {'name': '__jda', 'value': '259140492.15408908147411217583627.1540890815.1540890815.1540890815.1', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1556442827}, {'name': '__jdb', 'value': '259140492.2.15408908147411217583627|1.1540890815', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': 1540892627}, {'name': '__jdc', 'value': '259140492', 'path': '/', 'domain': '.yhd.com', 'secure': False, 'httpOnly': False, 'expiry': None}]"
        cookies_list = eval(cookies_str)

        for i in cookies_list:
            self.driver.add_cookie(i)

        self.driver.refresh()

        self.driver.find_element_by_xpath("html/body/div[2]/div[1]/div/div[3]/ul/li[4]/div/a/span").click()

        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

        assert "最近暂无订单" == self.driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div/div[2]/div/div[2]").text

        # try:
        #     # self.driver.find_element_by_partial_link_text("最近订单")
        #     # self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]")
        #     assert True
        # except Exception as e:
        #     assert False

