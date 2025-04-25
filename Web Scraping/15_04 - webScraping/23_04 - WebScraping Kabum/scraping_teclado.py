# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

emuladorChrome = "C:\chromedriver-win64\chromedriver.exe"

#Configuração do WebDriver
servico = Service(emuladorChrome)
controle = webdriver.ChromeOptions()
controle.add_argument('--disable-gpu')
controle.add_argument('--window-size=1920,1080')

# Inicializador do WebDriver
executador = webdriver.Chrome(service = servico, options = controle)

# URL inicial
url_site = 'https://www.kabum.com.br/perifericos/teclado-gamer'
executador.get(url_site)
time.sleep(5)

# Dicionário para inserir os títulos e preços
dic_produtos = {
    'Teclados mecânicos': [],
    'Preço': []
}

# Inicia na pág 1, incrementa a cada troca de pág
pag = 1

# Filtra os teclados com switch azul
try:
    btn_checkBox = WebDriverWait(executador, 5).until(
        ec.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='Blue']"))
    )
    if btn_checkBox:
            executador.execute_script('arguments[0].click();', btn_checkBox)
            print('---- Filtrando os teclados para os que tem switch azul ----')
            time.sleep(5)
    else:
        print('Não há check box com esse valor :/')
except Exception as e:
    print('Erro ao localizar a checkbox', e)



# Coleta os dados
while True:
    print(f'\n Coletando dados da página {pag}...')

    try:
        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'productCard'))
        )
        print('Elementos encontrados com sucesso!')
    except TimeoutException:
        print('Tempo de espera excedido')

    produtos = executador.find_elements(By.CLASS_NAME, 'productCard')

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, 'nameCard').text.strip()
            preco = produto.find_element(By.CLASS_NAME, 'priceCard').text.strip()
            print(f'{nome} - {preco}')

            dic_produtos['Teclados mecânicos'].append(nome)
            dic_produtos['Preço'].append(preco)
        
        except Exception:
            print('Erro ao coletar dados:', Exception)

# Encontrar botão da próxima página
    try:
        btn_prox = WebDriverWait(executador, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'nextLink'))
        )
        if btn_prox:
            executador.execute_script('arguments[0].scrollIntoView();', btn_prox)
            time.sleep(1)

            executador.execute_script('arguments[0].click();', btn_prox)
            print(f'Indo para a página {pag}')
            pag += 1
            time.sleep(5)
        else:
            print('Você chegou na última página')
            break
    except Exception as e:
        print('Erro ao tentar avançar para a próxima página ', e)
        break

# Frecha o navegador
executador.quit()

df = pd.DataFrame(dic_produtos)
df.to_excel('TecladosKabum.xlsx', index=False)

print(f'Arquivo "TecladosKabum" salvo com sucesso! ({len(df)} produtos capturados!)')