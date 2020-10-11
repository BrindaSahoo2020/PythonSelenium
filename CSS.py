#Selecting element by CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://cooking.stackexchange.com/")

#CSS selector by ID
elem = driver.find_element_by_css_selector("a#nav-questions")
print(elem.text)
elem.click()
time.sleep(1)

#CSS selector by Class Name
elem1 = driver.find_element_by_css_selector("a[class= 'pl8 js-gps-track nav-links--link']")
print(elem1.text)
time.sleep(1)

#CSS selector by Class Name
elem2 = driver.find_element_by_css_selector("a[class= 'login-link s-btn s-btn__filled py8 js-gps-track']")
print(elem2.text)
driver.back() #Navigate back
time.sleep(1)

#CSS selector by multiple Class Name
elem3 = driver.find_element_by_css_selector("a.ws-nowrap.s-btn.s-btn__primary")
print(elem3.text)
time.sleep(1)

#CSS with 2 attribute

elem4 = driver.find_element_by_css_selector("a[class='grid--cell s-btn s-btn__muted s-btn__outlined'][title='Questions that have been asked, answered, or updated recently']")
print(elem4.text)
time.sleep(1)
driver.quit()