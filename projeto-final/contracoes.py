from time import sleep
from selenium import webdriver as se
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import pyautogui as py
import pandas

navegador = se.Chrome()
navegador.get("https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1")

wordKeys = 'Dipirona sódica'

search = navegador.find_element(By.ID, 'keyword')

search.send_keys(wordKeys)

sleep(2)

checkBox = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[1]/div[2]/div/div[4]/div/label' )

checkBox.click()

sleep(5)

searchBtn = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button')


# def scroll_to_element(navegador):
#     iframe = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button' )
#     ActionChains(navegador) \
#         .scroll_to_element(iframe) \
#         .perform()
#
#     assert _in_viewport(navegador,iframe)
#
#
# def _in_viewport(driver, element):
#     script = (
#         "for(var e=arguments[0],f=e.offsetTop,t=e.offsetLeft,o=e.offsetWidth,n=e.offsetHeight;\n"
#         "e.offsetParent;)f+=(e=e.offsetParent).offsetTop,t+=e.offsetLeft;\n"
#         "return f<window.pageYOffset+window.innerHeight&&t<window.pageXOffset+window.innerWidth&&f+n>\n"
#         "window.pageYOffset&&t+o>window.pageXOffset"
#     )
#     return driver.execute_script(script, element)

# scroll_to_element(navegador)

sleep(5)
searchBtn.click()

sleep(5)

frameEditals = navegador.find_element(By.CLASS_NAME, 'br-list')
# edital = frameEditals.find_elements(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div/div[2]/pncp-items-list/div/div[1]/a')
edital = frameEditals.find_elements(By.XPATH, './/*[@tittle="Acessar item."]')

print(edital)


# edital.click()

for editalAtual in edital:
    links = editalAtual.get_attribute("href")
    print(links)

sleep(5)


