import pyautogui as pa

for i in range(0, 10):
    print(pa.position())
    pa.sleep(1)
#clica no menu iniciar
pa.moveTo(x=691, y=1059)
pa.sleep(1)
pa.click()
pa.sleep(1)

#pesquisa calculadora e abre
pa.write('Calc')
pa.press('enter')

## calculo
pa.moveTo(x=583, y=866)
pa.press('enter')

