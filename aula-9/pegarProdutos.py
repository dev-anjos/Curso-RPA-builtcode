from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as py

navegador = se.Chrome()
navegador.get("https://www.magazineluiza.com.br/")
sleep(2)

produto = 'placa de video'
produtos = []

search = navegador.find_element(By.ID, 'input-search')

search.send_keys(produto)
sleep(1)
py.press('enter')

sleep(3)
cardElemento = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/div/ul')
linhas = cardElemento.find_elements(By.TAG_NAME, 'li')

nomeProduto = []

for linhaAtual in linhas:
    nomeProduto = navegador.find_element(By.XPATH , '//*[@data-testid="product-title"]').text
    print(nomeProduto)
    produtos.append(linhaAtual.text)




#
# print(produtos)


sleep(4)





