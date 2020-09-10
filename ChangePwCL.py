from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#el rut utilizado fue sacado a través de un generador de rut falsos, al revisar este rut en un rutificador no arrojó información, por lo que aun no le corresponde a nadie.

driver = webdriver.Chrome('./chromedriver')
driver.get('https://simple.ripley.cl')
time.sleep(3)
driver.find_element_by_class_name('my-account').click()
time.sleep(3)
driver.find_element_by_class_name('credentials__link').click()
time.sleep(3)
driver.find_element_by_name('wc_username').send_keys('22528427k')
driver.find_element_by_class_name('btn-loading  btn-ripley').click()
time.sleep(3)
driver.quit()