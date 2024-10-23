from time import sleep

from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

navegador = se.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
sleep(2)

i = 1
while i < 4:

    linha = 1

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'TD')

    i = i + 1

    for linhaAtual in linhas:
        print(linhaAtual.text)
        linha = linha + 1

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    sleep(3)








