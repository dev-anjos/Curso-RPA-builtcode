from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as py
import pandas

dataFrame = pandas
navegador = se.Chrome()
navegador.get("https://www.magazineluiza.com.br/")
coluna = []
sleep(2)

produto = 'placa de video'
produtos = []
nomeP = []
precoP = []
linkP = []

search = navegador.find_element(By.ID, 'input-search')

search.send_keys(produto)
sleep(1)
py.press('enter')

sleep(3)
cardElemento = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/div/ul')
linhas = cardElemento.find_elements(By.TAG_NAME, 'li')


for linhaAtual in linhas:
    nomeProduto = linhaAtual.find_element(By.XPATH, './/*[@data-testid="product-title"]')
    preco = linhaAtual.find_element(By.XPATH, './/*[@data-testid="price-value"]')
    link = (linhaAtual.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/div/ul/li[1]/a').get_attribute("href"))


    # produtos.append(nomeProduto.text+";"+preco.text+";"+link)
    nomeP.append(nomeProduto.text)
    precoP.append(preco.text)
    linkP.append(link)



dataFrame = pandas.DataFrame({'Nome do produto': [nomeP] , 'preco': [precoP],  'link':[linkP]})

arquivoExcel = pandas.ExcelWriter('DadosSite.xlsx', engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name='sheel', index=False)
arquivoExcel._save()

print(produtos)

sleep(4)





