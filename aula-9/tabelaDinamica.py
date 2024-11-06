from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

navegador = se.Chrome()
navegador.get("https://rpachallenge.com/")
sleep(2)
#
# cep = 23932055

firstName = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]')
firstName.send_keys("Juan")
sleep(1)

lastName = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]')
lastName.send_keys("Pedro anjos da silva")

email = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]')
email.send_keys("juan@juan")

address = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]')
address.send_keys("Rua são joao da barra")

roleInCompany = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]')
roleInCompany.send_keys("Programador")

phoneNumber = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]')
phoneNumber.send_keys(24992704395)

companyName = navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]')
companyName.send_keys("Builtcode")

sleep(1)

btnSubmit = navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
btnSubmit.click()

sleep(5)









# navegador.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/div/a/button').click()
#
# endereco = []
#
# enderecoSite = navegador.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div[1]/div[2]')
#
# for e in enderecoSite:
#     print(e.text)
#
#
# sleep(1)
# # endereco.append(enderecoSite.text)
#
#
#
# sleep(2)

