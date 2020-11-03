'''Write a selenium webdriver script to perform the following in sequence:

Using chrome navigate directly to http://the-internet.herokuapp.com/challenging_dom
Highlight the text in the third row of the Diceret column for two seconds.
Highlight the delete link in the row containing “Apeirian7” for two seconds
Highlight the edit link for the row containing “Apeirian2” for two seconds.
Highlight “Definiebas7” for two seconds, then highlight “Iuvaret7” for two seconds.
Click the Green button.'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time

#Using chrome navigate directly to http://the-internet.herokuapp.com/challenging_dom
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://the-internet.herokuapp.com/challenging_dom")

#Highlight method and  style added
def highlight(element):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("background: pink;border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)
#Highlight the text in the third row of the Diceret column for two seconds.
elem = driver.find_element_by_xpath("//table/tbody/tr[3]/td[6]")
highlight(elem)
#Highlight the delete link in the row containing “Apeirian7” for two seconds.
el = driver.find_element_by_xpath("//table/tbody/tr[8]/td[7]")
elem1 = el.find_element_by_link_text("delete")
highlight(elem1)
#Highlight the edit link for the row containing “Apeirian2” for two seconds.
elm = driver.find_element_by_xpath("//table/tbody/tr[3]/td[7]")
elem2 = elm.find_element_by_link_text("edit")
highlight(elem2)
#Highlight “Definiebas7” for two seconds
elem3 =driver.find_element_by_xpath("//table/tbody/tr[8]/td[4]")
highlight(elem3)
# highlight “Iuvaret7” for two seconds.
elem4 =driver.find_element_by_xpath("//table/tbody/tr[8]/td[1]")
highlight(elem4)
time.sleep(1)
#Click the Green button.
button1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[1]/a[1]")
button2 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[1]/a[2]")
button3 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[1]/a[3]")
list_button = [button1,button2,button3]
for i in range(0,len(list_button)):
    button_color = Color.from_string(list_button[i].value_of_css_property('background-color')).hex
    if button_color == "#5da423":
         list_button[i].click()
         print("Green button clicked")
time.sleep(2)
driver.quit()
