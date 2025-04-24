import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site a ser acessado
url = 'http://books.toscrape.com/'

# Fazer a requisição HTTP
response = requests.get(url)

# Criar um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Criar um lista para armazenar os dados
books_data = []

# Encontra os elementos que contém a tag article e a classe product_pod
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a.attrs['title']
    price = book.find('p', class_='price_color').text
    books_data.append([title, price])

df = pd.DataFrame(books_data, columns=['Título', 'Preço'])

df.to_excel('livros.xlsx', index=False)

print('Dados salvos no arquivo livros.xlsx com sucesso!')