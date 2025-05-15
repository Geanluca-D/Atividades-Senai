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

# Configuração do Web driver
servico = Service(emuladorChrome)
controle = webdriver.ChromeOptions()
controle.add_argument('--disable-gpu')
controle.add_argument('--window-size=1920,1080')

# Inicializador do Web driver
executador = webdriver.Chrome(service = servico, options = controle)

# URL inicial
url_site = 'https://masander.github.io/AlimenticiaLTDA-financeiro/?authuser=0#/'
executador.get(url_site)
time.sleep(5)

# Coleta os dados
while True:
    print(f'\n Coletando dados da página')
#========================================= 1 tabela =================================================
    # Procura o elemento na página
    try:
        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.TAG_NAME, 'table'))
        )
        print('Tabela encontrada')
    except TimeoutException:
        print('Tempo de espera excedido!')

    # Acha a tabela e pega o HTML da tabela
    tabelaDesp = executador.find_element(By.TAG_NAME, "table")
    tabelaDesp_html = tabelaDesp.get_attribute('outerHTML')

    # Converte HMTL em DataFrame
    df = pd.read_html(tabelaDesp_html)[0]

#==================== Encontrar e clicar no botão da próxima página ===================================
   # Localiza o botão para trocar de página e clica nele
    try:
        btn_prox = WebDriverWait(executador, 5).until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Orçamentos']"))
        )
        if btn_prox:
            executador.execute_script('arguments[0].click();', btn_prox)
            print('Indo para próxima página...')
            time.sleep(5)
        else:
            print('Você chegou a última página')
            break
    except Exception as e:
        print('Erro ao localizar o botão ', e)
        break

#========================================= 2 tabela =================================================
    # Procura o elemento na página
    try:
        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.TAG_NAME, 'table'))
        )
        print('Tabela encontrada')
    except TimeoutException:
        print('Tempo de espera excedido!')

    # Acha a tabela e pega o HTML da tabela
    tabelaOrc = executador.find_element(By.TAG_NAME, "table")
    tabelaOrc_html = tabelaOrc.get_attribute('outerHTML')

    # Converte HMTL em DataFrame
    df2 = pd.read_html(tabelaOrc_html)[0]
    break

#===================================== Fecha o navegador ==============================================
executador.quit()

df.to_excel('despesas.xlsx', index=False)
df2.to_excel('orcamentos.xlsx', index=False)

print(f'Arquivos gerados!')