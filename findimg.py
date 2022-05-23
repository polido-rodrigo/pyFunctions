#Script que tenta localizar na tela uma imagem
#Retorna true se encontrar

#Parametros obrigatorios:

#img = string (caminho da imagem com a extensao - Ex: "/home/meunome/salvar.png")

#zona = int TUPLA (regiao da tela em que sera procurado - Ex: caso queira procurar uma imagem no quadrante superior esquerdo de um monitor full hd ultilize a tupla (0,0,960,540)

#desc = string (breve descricao da imagem - Ex: "Botao salvar")


#Parametros opcionais

#tentativas = int (define quantas tentativas para encontrar a imagem - Ex: 10)

#tentativas_interv_sec = int (define intervalo de tempo em segundos entre as tentativas - Ex: 1)

#clicar = bool (caso encontrar a imagem, define se sera efetuado o click no centro da imagem - Ex: True)

#problema = bool (caso nao encontrar a imagem, define se exibira uma msgbox com erro, voce tera a opcao de continuar ou parar o script)

from time import sleep
import pyautogui as pgui
import pymsgbox

def findimg(img, zona, desc, tentativas=10, tentativas_interv_sec=1, clicar= True, problema= True):
    #cursor no canto
    pgui.moveTo(5,5,duration =.1)

    alvo = pgui.locateCenterOnScreen(img, region = zona)
    ciclo_png = 0

    #Enquanto não encontra
    while alvo == None:
        if ciclo_png < tentativas:
            ciclo_png += 1
            print(f'{ciclo_png}/{tentativas} Tentativas de encontrar: {desc}','\r',end = '')
            alvo = pgui.locateCenterOnScreen(img, region = zona)
            sleep(tentativas_interv_sec)

        elif ciclo_png >= tentativas:
            print(f'\n{desc} NÃO encontrado(a)!\n')
            conti_png = ''
            if problema == True:
                conti_png = pymsgbox.confirm(f'Não foi possível encontrar {desc}!\n\nClique manualmente no(a) "{desc}" e depois clique em CONTINUAR para prosseguir o script.\n','Problema',['CONTINUAR','PARAR'])
                if conti_png != 'CONTINUAR' :
                    print('Finalizando o script...')
                    exit()
            else:
                print('Continuando o script...')
            return False
        
    #Quando sai do loop
    if alvo != None:
        print(f'\n{desc} Encontrado(a)\n')
        pgui.moveTo(alvo, duration = 0.1)
        if clicar == True:
            pgui.click(alvo)
        #cursor no canto
        pgui.moveTo(5,5,duration =.1)
        return True