#Mouse Hover using Selenium Python

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MouseHover(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.sanfoundry.com/")
    def test_hover(self):
        timeout = 30
        driver = self.driver
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='header-image']")))
        except TimeoutException:
            print("wait till the page is not loaded")
        elem = driver.find_element_by_link_text("Home")
        ActionChains(driver).move_to_element(elem).perform()
        time.sleep(5)
    def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()