from selenium import webdriver
import time
import random

Nombre = ("JUAN", "JOSE LUIS","JOSE","MARIA"," GUADALUPE","FRANCISCO","GUADALUPE","MARIA JUANA","ANTONIO","JESUS","MIGUEL","ANGEL","PEDRO","ALEJANDRO","MANUEL","MARGARITA","MARIA DEL CARMEN", "CARLOS","ROBERTO","FERNANDO","DANIEL")
Apellido = ("Abad", "Abadia", "Abarca", "Abastos", "Abaunza","Abbot", "Abdalla", "Abdalah", "Abdallah", "Abdelnour","Abdo", "Abea", "Abel", "Abela", "Abelado", "Abella","Abellan", "Abendaño", "Abou", "Abraham", "Abrahams")

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eldiario.es/')
time.sleep(3)
driver.find_element_by_class_name('login').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/p/a').click()
time.sleep(3)
driver.find_element_by_name('email').send_keys('hola67@gmail.com')
driver.find_element_by_name('userAgree').click()
time.sleep(1)
driver.find_element_by_id('btnSubmit').click()
time.sleep(3)
driver.find_element_by_id('name').send_keys(random.choice(Nombre))
driver.find_element_by_name('surname').send_keys(random.choice(Apellido))
driver.find_element_by_name('pw').send_keys('P4$$w rd!')
time.sleep(3)
driver.find_element_by_id('btnSubmit').click()

time.sleep(6)
driver.quit()