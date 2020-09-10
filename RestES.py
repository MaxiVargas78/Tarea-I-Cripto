#restablecimiento de contraseña
from selenium import webdriver
import time
import random

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eldiario.es/')
time.sleep(3)
driver.find_element_by_class_name('login').click()
time.sleep(6)
driver.find_element_by_class_name('login__forgot-password').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name('email').click()
driver.find_element_by_name('email').send_keys('maxx7689@hotmail.com')
time.sleep(2)
driver.find_element_by_id('btnSubmit').click()
time.sleep(6)
driver.quit()

