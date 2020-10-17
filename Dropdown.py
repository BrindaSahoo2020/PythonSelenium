#Select drop down by Selenium-python

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select 

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

elem_indus = driver.find_element_by_name("Industry")
select = Select(elem_indus)
select.select_by_visible_text('Aerospace')
select.select_by_value('health')
select.select_by_index(2)

select.is_multiple   #It says whether it can select multiple values or single values ,does not return anything
print(select.is_multiple)
driver.quit()