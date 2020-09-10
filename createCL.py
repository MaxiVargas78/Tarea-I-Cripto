from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#los rut utilizados fueron sacados a través de un generador de rut falsos

Nombre = ("JUAN", "JOSE LUIS","JOSE","MARIA"," GUADALUPE","FRANCISCO","GUADALUPE","MARIA JUANA","ANTONIO","JESUS","MIGUEL","ANGEL","PEDRO","ALEJANDRO","MANUEL","MARGARITA","MARIA DEL CARMEN", "CARLOS","ROBERTO","FERNANDO","DANIEL")
Apellido = ("Abad", "Abadia", "Abarca", "Abastos", "Abaunza","Abbot", "Abdalla", "Abdalah", "Abdallah", "Abdelnour","Abdo", "Abea", "Abel", "Abela", "Abelado", "Abella","Abellan", "Abendaño", "Abou", "Abraham", "Abrahams")
RUT = ("215127761", "122874281","84289426","120001809","22236759k","143074110","126727240","122805298","86946777","145552613")


driver = webdriver.Chrome('./chromedriver')
driver.get('https://simple.ripley.cl')
time.sleep(3)
driver.find_element_by_class_name('my-account').click()
time.sleep(3)
driver.find_element_by_class_name('signup__link').click()
driver.find_element_by_name('firstName').send_keys(random.choice(Nombre))
driver.find_element_by_name('lastName').send_keys(random.choice(Apellido))
driver.find_element_by_name('ws_username').send_keys(random.choice(RUT))
driver.find_element_by_name('email').send_keys('hola@hola.cl')
driver.find_element_by_name('password').send_keys('P4$$w rd!')
driver.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()

