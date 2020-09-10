from selenium import webdriver
import time
import random

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eldiario.es/')
time.sleep(3)
driver.find_element_by_class_name('login').click()
time.sleep(6)
driver.find_element_by_name('email').send_keys('maxx7689@hotmail.com')
driver.find_element_by_name('password').send_keys('P4$$w rd!')
time.sleep(2)
driver.find_element_by_class_name('login__button').click()
time.sleep(10)
driver.quit()
