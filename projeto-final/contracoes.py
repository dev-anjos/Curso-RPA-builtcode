from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as py
import pandas

# def scroll_to_element(navegador,elementXpath ):
#     iframe = elementXpath
#     ActionChains(navegador) \
#         .scroll_to_element(iframe) \
#         .perform()

#     assert _in_viewport(navegador,iframe)


# def _in_viewport(driver, element):
#     script = (
#         "for(var e=arguments[0],f=e.offsetTop,t=e.offsetLeft,o=e.offsetWidth,n=e.offsetHeight;\n"
#         "e.offsetParent;)f+=(e=e.offsetParent).offsetTop,t+=e.offsetLeft;\n"
#         "return f<window.pageYOffset+window.innerHeight&&t<window.pageXOffset+window.innerWidth&&f+n>\n"
#         "window.pageYOffset&&t+o>window.pageXOffset"
#     )
#     return driver.execute_script(script, element)

scrollToElement = "arguments[0].scrollIntoView({ block: 'center' });"

navegador = se.Chrome()

wordKeys = ["Dipirona Sódica", "Clonazepam", "Atenalol"]

for keys in wordKeys:

    navegador.get("https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1")

    search = navegador.find_element(By.ID, 'keyword')

    search.send_keys(keys)
    sleep(2)

    checkBox = (
        navegador.find_element(By.XPATH,'//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[1]/div[2]/div/div[4]/div/label'))

    checkBox.click()

    sleep(5)

    searchBtn = (
        navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button'))

    navegador.execute_script(scrollToElement, searchBtn)

    sleep(5)
    searchBtn.click()

    sleep(5)

    frameEditals = (
        navegador.find_element(By.XPATH,'//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div/div[2]/pncp-items-list'))


    numberOfResults = navegador.find_element(By.XPATH, './/*[@id="tam_pagina"]')
    navegador.execute_script(scrollToElement, numberOfResults)
    numberOfResults.click()
    cemResults = numberOfResults.find_element(By.XPATH, './/*[@title="100"]')
    cemResults.click()

    links = []
    text = []

    for x in frameEditals.find_elements(By.XPATH, '//*[@title= "Acessar item."]'):
        link = x.get_attribute("href")
        links.append(link)

    # btnNext = navegador.find_element(By.XPATH, './/*[@data-next-page="data-next-page"]')
    # btnNext.click()

    for link in links:
        navegador.get(link)
        sleep(10)
        try:
            buttonDetail = WebDriverWait(navegador, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="br-button circle ng-star-inserted"]'))
            )
        except Exception as e:
            print("Erro ao carrega detalhes do edital")

        print(f"abriu o site: {link}")

        buttonDetail = navegador.find_elements(By.XPATH, '//*[@class="br-button circle ng-star-inserted"]')
        sleep(2)

        # tableItens = navegador.find_element(By.XPATH, '//*[@title="Itens"]')
        for btn in buttonDetail:
            sleep(5)
            navegador.execute_script(scrollToElement, btn)
            btn.click()
            ##aqui pegará os dados
            modalDetail = navegador.find_element(By.XPATH, '//*[@class="br-card"]')
            # textItem = modalDetail.find_elements(By.TAG_NAME, "span")

            for modal in modalDetail:
                span = modal.find_elements(By.TAG_NAME, "span")
                text.append(span.text)


            print(text)
            sleep(2)
            btnReturn = navegador.find_element(By.XPATH, '//*[@class="br-button primary small m-2"]')

            btnReturn.click()
            sleep(2)

            sleep(2)

    print(links)




sleep(5)
