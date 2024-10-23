import pyautogui as py

opcaoEscolhida = py.confirm(text='Escolha uma opção', buttons=['Bloco de notas', 'Calculadora', 'Chrome'])


if opcaoEscolhida == 'Bloco de notas':
    py.hotkey(['win', 'r'])
    py.typewrite(['notepad', 'enter'])
elif opcaoEscolhida == 'Calculadora':
    py.hotkey(['win', 'r'])
    py.typewrite(['calc', 'enter'])
elif opcaoEscolhida == 'Chrome':
    py.hotkey(['win', 'r'])
    py.typewrite(['chrome', 'enter'])



