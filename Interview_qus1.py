'''
Write a selenium webdriver script to perform the following :

Using Chrome navigate directly to http://the-internet.herokuapp.com
Follow the link titled "frames"
Follow the link to "nested frames"
print the text in each frame in the following order.
bottom
middle
left
right
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Using Chrome navigate directly to http://the-internet.herokuapp.com
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://the-internet.herokuapp.com")

#Scroll down to get the link Frames
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform() 
time.sleep(2)
#Follow the link titled "frames" -> Follow the link to "nested frames"
frames = driver.find_element_by_link_text("Frames")
frames.click()
time.sleep(1)
nested_frames = driver.find_element_by_link_text("Nested Frames")
nested_frames.click()
time.sleep(1)
#print the text in each frame in the following order(bottom,middle,left,right)

driver.switch_to.frame("frame-bottom")
time.sleep(1)
frameContent1 = driver.find_element_by_xpath("/html/body")
print(frameContent1.text)
driver.quit()