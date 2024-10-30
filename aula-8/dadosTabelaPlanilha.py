from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas

navegador = se.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net/")
sleep(2)
dataFrame = pandas
dataFrameLista = []

i = 1
while i < 4:

    # linha = 1

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]/tbody')

    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    i = i + 1

    for linhaAtual in linhas:
        print(linhaAtual.text)
        dataFrameLista.append(linhaAtual.text)

        dataFrame = pandas.DataFrame(dataFrameLista, columns=['Nome_coluna'])
        # linha = linha + 1

    arquivoExcel = pandas.ExcelWriter('DadosSite.xlsx', engine='xlsxwriter')
    dataFrame.to_excel(arquivoExcel, sheet_name='sheel', index=False)
    arquivoExcel._save()

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    sleep(3)








