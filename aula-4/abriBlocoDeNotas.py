import pyautogui as py

py.hotkey(['win', 'r'])
py.typewrite(['notepad', 'enter'])

py.sleep(1)
py.typewrite('teste')
