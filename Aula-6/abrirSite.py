from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

navegador = se.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

sleep(2)

(navegador.find_element(By.ID, "first_3")
    .send_keys("Juan "))

sleep(1)

(navegador.find_element(By.ID, "last_3")
 .send_keys("Pedro anjos da silva"))

(navegador.find_element(By.XPATH, "//*[@id='input_4']")
    .send_keys("juanpedro_0@hotmail.com"))

sleep(1)

idDropDown = navegador.find_element(By.ID, "input_5")
selectItem = Select(idDropDown)
selectItem.select_by_index(1)