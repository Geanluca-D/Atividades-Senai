import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Configuração inicial
st.set_page_config(page_title='Dashboard de Vendas', page_icon='🥸', layout='wide')

# Carregar dados
df = pd.read_excel('Vendas.xlsx')

# Filtros:
# Sidebar
st.sidebar.header('Selecione os filtros')

# Filtro por loja
lojas = st.sidebar.multiselect(
    'Lojas',
    options = df['ID Loja'].unique(), # Opção do filtro
    default = df['ID Loja'].unique(), # Opção que vem por padrão no filtro
    key = 'loja' # Chave única
)

# Filtro de produto
produtos = st.sidebar.multiselect(
    'Produtos',
    options = df['Produto'].unique(),
    default = df['Produto'].unique(),
    key = 'prduto'
)

# Filtrar o dataframe de acordo com as opções selecionadas
df_selecao = df.query('`ID Loja` in @lojas and Produto in @produtos')

# Gráficos e na função da página
def home():
    st.title('Faturamento das lojas')
    total_vendas = df['Quantidade'].sum()
    media = df['Quantidade'].mean()
    mediana = df['Quantidade'].median()

    total1, total2, total3 = st.columns(3)
    with total1:
        # Apresentar indicadores rápidos
        st.metric('Total Vendido 💰', value=int(total_vendas))
    with total2:
        st.metric('Média por Produto', value=f'{media:.2f}')
    with total3:
        st.metric('Mediana', value=int(mediana))

    st.markdown('---')

def graficos():
    # Criar um grafico de barras, mostrando a quantidade de produtos por loja
    fig_barras = px.bar(
        df_selecao,
        x='Produto',
        y='Quantidade',
        color='ID Loja',
        barmode='group',
        title='Quantidade de produtos vendidos por loja'
    )

    # Gráfico de linha, com o total de vendas por loja
    fig_linha = px.line(
        df_selecao.groupby(['ID Loja']).sum(numeric_only=True).reset_index(),
        x='ID Loja',
        y='Quantidade',
        title='Total de vendas por loja'
    )

    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(fig_barras, use_container_width=True)
    with graf2:
        st.plotly_chart(fig_linha, use_container_width=True)
    
def sideBar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Home', 'Gráficos'],
            icons=['house', 'bar-chart'],
            default_index=0
        )

    if selecionado == 'Home':
        home()
        graficos()
    elif selecionado == 'Gráficos':
        graficos()

sideBar()