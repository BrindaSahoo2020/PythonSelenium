#Add cookies and cont the number by sing Action chain

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ActionChain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://orteil.dashnet.org/cookieclicker/")
    def test1(self):
        timeout = 30
        driver = self.driver
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='bakeryName']")))
        except TimeoutException:
            print("wait till the page is not loaded")
        cookie = driver.find_element_by_id("bigCookie")
        actions = ActionChains(driver)
        actions.click(cookie)
        count = driver.find_element_by_id("cookies")
        for i in range(10):
            actions.perform()
            print(count.text)
            time.sleep(2)
    def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()