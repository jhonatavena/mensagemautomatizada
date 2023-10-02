import pyautogui
from time import sleep

with open('grupos.txt', 'r') as file:
    grupos = file.readlines()


for grupo_nome in grupos:
    grupo_nome = grupo_nome.strip()
    mensagem = 'sua mensgame'  

    pyautogui.click(-1151, 435, duration=0.5)
    
    pyautogui.write(grupo_nome)
    pyautogui.click(-1151, 494, duration=0.5)

    pyautogui.click(-660, 1055, duration=1)

    pyautogui.write(mensagem)

    pyautogui.click(-46, 1057)
    
    print(f'Mensagem enviada para o grupo: {grupo_nome}')
    
    sleep(1)  

print('FINALIZADO')
