from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import csv
import pyautogui as py

#funcao para realizar scroll
scrollToElement = "arguments[0].scrollIntoView({ block: 'center' });"

## Configurações
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions") 
options.add_argument("--no-sandbox") 

navegador = webdriver.Chrome(options=options)
navegador.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

wordKeys = py.prompt(text='Digite os textos a serem pesquisados (separe por virgula)', title='Pesquisa de Editais' , default='Dipirona Sódica, Atenolol, Clonazepam')
wordKeys = wordKeys.split(',')
wordKeys = [key.strip() for key in wordKeys]

for keys in wordKeys:
    navegador.get("https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1")

    sleep(2)
    search = navegador.find_element(By.ID, 'keyword')
    search.send_keys(keys)
    sleep(2)

    checkBox = (
        navegador.find_element(By.XPATH,'//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[1]/div[2]/div/div[4]/div/label'))
    checkBox.click()
    sleep(2)

    searchBtn = (
        navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button'))
    navegador.execute_script(scrollToElement, searchBtn)
    sleep(2)
    searchBtn.click()
    sleep(2)

    numberOfResults = navegador.find_element(By.XPATH, './/*[@id="tam_pagina"]')
    navegador.execute_script(scrollToElement, numberOfResults)
    sleep(2)

    numberOfResults.click()
    hundredResults = numberOfResults.find_element(By.XPATH, './/*[@title="100"]')
    sleep(2)
    hundredResults.click()

    links = []
    itens = []
    limitOfLinks = 2

    sleep(2)
    frameEditals = (
        navegador.find_element(By.XPATH,'//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div/div[2]/pncp-items-list')
    )

    while len(links) < limitOfLinks:
        sleep(5)
        for i, x in enumerate(frameEditals.find_elements(By.XPATH, '//*[@title= "Acessar item."]')):
            if i >= 2: #contador adicionado pois o elemento se repete 300 vezes na pagina, portanto a cada 100 ele vai para a proxima pagina
                break
            link = x.get_attribute("href")
            links += [link]
            i += 1

        print(f"Coletados {len(links)} editais da palavra {keys}\n")

        nextPage = navegador.find_element(By.XPATH, '//*[@data-next-page="data-next-page"]')
        sleep(5)
        navegador.execute_script(scrollToElement, nextPage)
        sleep(5)
        nextPage.click()

    for link in tqdm(links, desc=f"Abrindo editais da palavra {keys}: ", colour="green", unit="editais"):
        navegador.get(link)
        sleep(5)
     
        try:
            buttonDetail = WebDriverWait(navegador, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="br-button circle ng-star-inserted"]'))
            )

            numberOfResults = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-footer/div/pncp-pagination-table/div/div[1]/pncp-select/div[2]')
            navegador.execute_script(scrollToElement, numberOfResults)
            sleep(2)
            numberOfResults.click()
            sleep(2)

            fiftyResults = numberOfResults.find_element(By.XPATH, '//*[@class="scrollable-content"]/div/span[text()="50"]')
            sleep(2)
            fiftyResults.click()

            sleep(5)
            headerOfTable = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-header/div')
            navegador.execute_script(scrollToElement, headerOfTable)
            sleep(5)

        except Exception as e:
            print(f"Erro ao carrega detalhes do edital: {e}")

        buttonDetail = navegador.find_elements(By.XPATH, '//*[@class="br-button circle ng-star-inserted"]')
        sleep(2)
    
        def get_element_text(element_path):
            try:
                return modalDetail.find_element(By.XPATH, element_path).text
            except NoSuchElementException:
                return "N/D"

        for btn in buttonDetail:
        
            navegador.execute_script(scrollToElement, btn)
            sleep(1)
            btn.click()
            modalDetail = navegador.find_element(By.XPATH, '//*[@class="br-modal-body"]')
            try:
                sleep(6)
                itemN =  get_element_text( '/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[1]')
                descricao = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[2]/div/p/span')
                criterio = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[3]/div[1]/p/span')
                situacao = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[3]/div[2]/p/span')
                tipo = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[3]/div[3]/p/span')
                categoria = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[3]/div[4]/p/span')
                incentivo = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[4]/div[1]/p/span')
                beneficio = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[4]/div[2]/p/span')
                margemNormal = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[4]/div[3]/p/span')
                margemAdicional = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[4]/div[4]/p/span')
                quantidade = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[5]/div[1]/p/span')
                unidadeMedida = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[5]/div[2]/p/span')
                valorUnitarioEstimado = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[5]/div[3]/p/span')
                valorTotalEstimado = get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[5]/div[4]/p/span')
                
                ## Resultado Edital
                ordemClassificacao = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[1]/div[1]/p/span')
                dataHomologacao = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[1]/div[2]/p/span')
                CNPJCPFNidentificacao = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[2]/div[1]/p/span')
                nomeFornecedor = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[2]/div[3]/p/span')
                indicadorSubcontratacao = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[3]/div[1]/p/span')
                porteEmpresa = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[3]/div[2]/p/span')
                codigoPais = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[3]/div[3]/p/span')
                usoMargemPreferencia = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[4]/div[1]/p/span')
                usoBeneficio = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[4]/div[2]/p/span')
                criterioDesempate = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[4]/div[3]/p/span')
                quantidadeHomologada=get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[5]/div[1]/p/span')
                valorUnitHomologado = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[5]/div[2]/p/span')
                valorTotalHomologado = get_element_text('//html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[5]/div[3]/p/span')
                percentualDescontoJulgamento =  get_element_text('/html/body/modal-container/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div[6]/div/p/span')
                    
                item = [
                    {
                        "item": itemN,
                        "descricao": descricao,
                        "criterio": criterio,
                        "situacao": situacao,
                        "tipo": tipo,
                        "categoria": categoria,
                        "incentivo": incentivo,
                        "beneficio": beneficio,
                        "margemNormal": margemNormal,
                        "margemAdicional": margemAdicional,
                        "quantidade": quantidade,
                        "unidadeMedida": unidadeMedida,
                        "valorUnitarioEstimado": valorUnitarioEstimado,
                        "valorTotalEstimado": valorTotalEstimado,
                        "ordemClassificacao": ordemClassificacao,
                        "dataHomologacao": dataHomologacao,
                        "situacao": situacao,
                        "CNPJCPFNidentificacao": CNPJCPFNidentificacao,
                        "nomeFornecedor": nomeFornecedor,
                        "indicadorSubcontratacao": indicadorSubcontratacao,
                        "porteEmpresa": porteEmpresa,
                        "codigoPais": codigoPais,
                        "usoMargemPreferencia": usoMargemPreferencia,
                        "usoBeneficio": usoBeneficio,
                        "criterioDesempate": criterioDesempate,
                        "quantidadeHomologada": quantidadeHomologada,
                        "valorUnitHomologado": valorUnitHomologado,
                        "valorTotalHomologado": valorTotalHomologado,
                        "percentualDescontoJulgamento": percentualDescontoJulgamento
                    }
                ]
                itens.append(item)
            except Exception as e:
                print(f"Não foi possivel pegar o item: {e}")
    
            sleep(2)
            btnReturn = navegador.find_element(By.XPATH, '//*[@class="br-button primary small m-2"]')
            sleep(1)
            btnReturn.click()
            sleep(2)

arquivo_csv = F'dados/dados{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'

with open(arquivo_csv, mode='x', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    cabecalhos = itens[0][0].keys() 
    writer.writerow(cabecalhos)
    
    for item_list in itens:
        for item in item_list:
            valores = item.values()  
            writer.writerow(valores)

print(f"CSV '{arquivo_csv}' criado com sucesso!")
