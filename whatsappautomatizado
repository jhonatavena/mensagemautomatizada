import pyautogui
from time import sleep

from colorama import init,Fore, Back
init()

#**ATENCAO** ANTES DE USAR DEVE COPIAR A MENSAGEM QUE DEVE SER ENVIADA PRIMEIRO
# A mensagem enviada e a que esta na area de trasnferencia 

with open('grupos.txt', 'r', encoding='utf-8') as file:
    grupos = file.readlines()

for grupo_nome in grupos:
    grupo_nome = grupo_nome.strip()

    # barra de pesquisa
    pyautogui.click(-1303, 41, duration=0.5)

    # nome do grupo
    pyautogui.write(grupo_nome)
    sleep(1)  

    # primeira opção
    pyautogui.click(-1430, 100, duration=0.5)
    sleep(1)  

    # campo da mensgame
    pyautogui.click(-518, 745, duration=0.5)
    sleep(1)

    # colando a mensagem no ctrl+ v
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)

    # enviando a mensagme
    pyautogui.press('enter')
    sleep(1)

    print(Fore.GREEN + f'Mensagem enviada para o grupo: {grupo_nome}')

    sleep(1)

print(Back.RED + 'FINALIZADO')
