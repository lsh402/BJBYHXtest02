import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.yhd.com/")

time.sleep(20)
print(driver.get_cookies())

driver.quit()