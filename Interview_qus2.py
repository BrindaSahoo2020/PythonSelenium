'''
Write a selenium webdriver script to perform the following

Using Chrome navigate directly to http://the-internet.herokuapp.com/dynamic_loading/2
Click "Start"
When the loading has finished, read and print the text that is displayed.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
#Using Chrome navigate directly to http://the-internet.herokuapp.com/dynamic_loading/2
driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")

#Click "Start", identified the webelement using xpath
driver.find_element_by_xpath("//*[@id='start']/button").click()

#Explictly wait until the text is visible or max timeout of 20sec is elapsed
wait = WebDriverWait(driver,20)

#When the loading has finished, read and print the text that is displayed.

try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))

except Exception as e:
    print("Web element is not found")

elem = driver.find_element_by_xpath("//div[@id='finish']/h4")
print(elem.text)
driver.quit()