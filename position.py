#Scrip que coleta 2 pontos na tela como referencia a posição atual do mouse e exibe a diferenca de pixels em X, Y entre os pontos, ideal pra quem quer coletar as cordenadas de um espaco na tela para usar no parametro region na funcao pyautogui.locateOnScreen()

import pyautogui as pgui
import pymsgbox

print('ENTER para capturar ou qualquer tecla para sair...')
continua = 'Sim'
p = 0
while continua == 'Sim':
    pymsgbox.alert('Posicione o mouse sobre o primeiro ponto e aperte ENTER')
    ponto01 = pgui.position()
    pymsgbox.alert('Posicione o mouse sobre o segundo ponto e aperte ENTER')
    ponto02 = pgui.position()
    p += 1
    resul = f'Ponto{p}:({ponto01[0]}, {ponto01[1]}, {ponto02[0]-ponto01[0]}, {ponto02[1]-ponto01[1]})'
    print(resul)
    continua = pymsgbox.confirm(f'{resul}\nVocê deseja pegar outro ponto?','Proximo?',['Sim',"Não"])

