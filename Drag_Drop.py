#Drag and Drop using Selenium Python

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DragDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    def test_drag(self):
        timeout = 30
        driver = self.driver
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_3dGepu']")))
        except TimeoutException:
            print("wait till the page is not loaded")
        #Drag the price bar and drop it at your price budget 
        source = driver.find_element_by_xpath("//div[@class='_3aQU3C']")
        target = driver.find_element_by_xpath("//div[@class='_3G9WVX _2N3EuE']")
        ActionChains(driver).drag_and_drop(source, target).perform()
        time.sleep(5)
        #Other method
        leftSlider = driver.find_element_by_class_name("_3aQU3C")
        ActionChains(driver).drag_and_drop_by_offset(leftSlider, 100, 0).perform()
        time.sleep(5)	
    def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()







