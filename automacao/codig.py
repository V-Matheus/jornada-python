# Passo a passo do sistema
# Passo 1: Acessar o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/tabela

import pyautogui
import time
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir no chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

# entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=798, y=477)
pyautogui.write('victormatheus507@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')

time.sleep(2)


# Passo 3: Importar a base de dados de produtos
import pandas

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto

    pyautogui.click(x=710, y=311)
    # Prencher o campos

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos