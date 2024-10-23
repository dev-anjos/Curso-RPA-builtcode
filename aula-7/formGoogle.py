from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

navegador = se.Chrome()

navegador.get("https://forms.gle/8UHHVcFBRuPqCqQP7")

sleep(2)

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    .send_keys("juanpedro_0@hotmail.com"))

sleep(1)

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
 .send_keys("Juan"))

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    .send_keys("Pedro anjos da silva"))

sleep(1)

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    .click())

sleep(3)

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]')
    .click())

sleep(3)

navegador.find_element(By.XPATH, '//*[@id="i24"]').click()

navegador.find_element(By.ID, 'i35').click()
navegador.find_element(By.ID, 'i47').click()

sleep(3)

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[5]/div[2]')
    .click())

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div')
    .click())

(navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div')
    .click())

navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

sleep(5)