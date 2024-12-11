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
navegador.get("https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1")
wordKeys = 'Dipirona sódica'

search = navegador.find_element(By.ID, 'keyword')
search.send_keys(wordKeys)

sleep(2)

checkBox = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[1]/div[2]/div/div[4]/div/label' )
checkBox.click()

sleep(5)

searchBtn = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button')
# searchBtn = '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button'


navegador.execute_script(scrollToElement, searchBtn)
# scroll_to_element(navegador,searchBtn)

sleep(5)
searchBtn.click()

sleep(5)

frameEditals = navegador.find_element(By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div/div[2]/pncp-items-list')
links = []
for x in frameEditals.find_elements(By.XPATH, '//*[@title= "Acessar item."]'):
    link = x.get_attribute("href")
    links.append(link)

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
    tableItens = navegador.find_element(By.XPATH, '//*[@title="Itens"]')
    # itens = navegador.find_element
    for btn in buttonDetail:
        sleep(5)
        navegador.execute_script(scrollToElement, tableItens)
        btn.click()
        ##aqui pegará os dados
        sleep(2)
        btnReturn = navegador.find_element(By.XPATH, '//*[@class="br-button primary small m-2"]')
  
        btnReturn.click()
        sleep(2)

    sleep(2)
   

    


print(links)
# sleep(5)


