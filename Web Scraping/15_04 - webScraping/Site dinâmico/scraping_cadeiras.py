#Módulo para controlar navegador
from selenium import webdriver

#Localizador de elementos
from selenium.webdriver.common.by import By

#Serviço para configurar caminho do executavel chrome driver
from selenium.webdriver.chrome.service import Service

#Classe que permite executar ações avançadas(mover mouse, clicar e arrastar etc)
from selenium.webdriver.common.action_chains import ActionChains

#Classe que espera de forma explicita até que a condição seja satisfeita(elemento aparecer)
from selenium.webdriver.support.ui import WebDriverWait

#Condições esperadas usadas com WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Trabalhar com dataframe
import pandas as pd

#Funções de tempo
import time

#Tratamento de excessão
from selenium.common.exceptions import TimeoutException


#Definir caminho do WebDriver
chrome_driver_path = "C:\chromedriver-win64\chromedriver.exe"


#Configuração WebDriver
servico = Service(chrome_driver_path) #Navegador controlado pelo selenium
controle = webdriver.ChromeOptions() #Configurar opções do navegador
controle.add_argument('--disable-gpu') #Evita possíveis erros gráficos
controle.add_argument('--window-size=1920,1080')
# controle.add_argument('--headless') - Executa sem exibir na tela

#Inicialização do WebDriver
executador = webdriver.Chrome(service=servico, options=controle)

# URL inicial - Inicia o site
url_site = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
executador.get(url_site)
time.sleep(5) #aguarda 5 segundos para garantir que a pagina carregue

#criar dicionário vazio para armazenar nomes e preços das cadeiras
dic_produtos = { 'Título':[],
                 'Preco':[] }

#Vamos iniciar na pagina 1 e ir incrementando em cada troca de pagina
pagina = 1

while True:
    print(f'\n Coletando dados da página {pagina}...')
    
    try:
    
        #webdriverwait cria uma espera de até 10 seg
        #until faz com que o código espere até qiue a condição seja verdadeira
        #ec.resence_of_all_elements_located verifica se todos os elemnetos 'productcard' estão acessiveis
        #By.Class indica que a busca será feita através da classe CSS de valor 'productcard'

        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'productCard'))
        )
        print('Elementos encontrados com sucesso')
    except TimeoutException:
        print('Tempo de espera excedido')

    produtos = executador.find_elements(By.CLASS_NAME, 'productCard')

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, 'nameCard').text.strip()
            preco = produto.find_element(By.CLASS_NAME, 'priceCard').text.strip()

            print(f'{nome} - {preco}')

            dic_produtos['Título'].append(nome)
            dic_produtos['Preco'].append(preco)

        except Exception:
            print('Erro ao coletar dados:', Exception)

    #Encontar botão da próxima página
    try:
        btn_proximo = WebDriverWait(executador, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'nextLink'))
        )
        #Encontrar o elemento:
        if btn_proximo:
            executador.execute_script('arguments[0].scrollIntoView();', btn_proximo)
            time.sleep(1)

            #Clilcar no botão 
            executador.execute_script('arguments[0].click();', btn_proximo)
            print(f'Indo para a página {pagina}')
            pagina += 1
            time.sleep(5)
        else:
            print('Você chegou na última página')
            break
    except Exception as e:
        print('Erro ao tentar avançar para a próxima página ', e)
        break

#Fecha o navegaor
executador.quit()

df = pd.DataFrame(dic_produtos)
df.to_excel('CadeirasKabum.xlsx', index=False)

print(f'Arquivo "CadeirasKabum" salvo com sucesso! ({len(df)} produtos capturados!)')