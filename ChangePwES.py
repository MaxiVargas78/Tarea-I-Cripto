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
time.sleep(6)
driver.find_element_by_class_name('user').click()
time.sleep(6)
driver.find_element_by_class_name('login-user').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[6]/div/div[1]/form/div[2]/div/div/span').click()
time.sleep(2)
driver.find_element_by_name('currentPassword').send_keys('P4$$w rd!')
driver.find_element_by_name('newPassword').send_keys('P4$$w rd!')
driver.find_element_by_class_name('profile-account__form-save').click()
time.sleep(3)
driver.quit()

