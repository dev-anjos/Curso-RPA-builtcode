from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

navegador = se.Chrome()
navegador.get("https://www.siterastreio.com.br/cep")
sleep(2)

cep = '23934010'

navegador.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/div/input').send_keys(cep)

navegador.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/div/a/button').click()

endereco = []

enderecoSite = navegador.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/h2')

for teste in enderecoSite:
    enderecoSite.append(endereco.)

print(endereco)


sleep(1)
# endereco.append(enderecoSite.text)



sleep(2)


