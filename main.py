import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import operator
from pandas import DataFrame
import matplotlib.patches as patches
from streamlit.hashing import _CodeHasher
#%matplotlib inline


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modalTraining = st.beta_container()

try:
    # Before Streamlit 0.65
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server

except ModuleNotFoundError:
    # After Streamlit 0.65
    from streamlit.report_thread import get_report_ctx
    from streamlit.server.server import Server

def main():
    state = _get_state()
    pages = {
        "Letra A": page_dashboard,
        "Letra B": page_settings,
        "Letra C": page_dashboard2,
        "Letra D": page_settings2,
        "Letra E": page_dashboard3,
        "Letra F": page_settings3,
        "Letra G": page_dashboard4,
        "Letra H": page_settings4,
        "Letra I": page_dashboard5,
        "Letra K": page_settings5,
    }

    st.sidebar.title("Ciência de Dados")
    page = st.sidebar.radio("Selecione o gráfico", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page](state)

    # Mandatory to avoid rollbacks with widgets, must be called at the end of your app
    state.sync()

def page_dashboard(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Total de vendas por ano:')
    #dados_vendas = pd.read_csv("Vendas2.csv")
    
    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    df['concatena'] = df.apply(lambda x: x['Data Venda']+'-'+x['ValorVenda'], axis=1)

    concatena = df['concatena']
    ano = []
    dados = []
    quantidades = []
    cont = 0


    for indice in concatena:
        
        valor = indice.split("-")
        dados.append(valor)
        tempAno = valor[0].split("/")
        
        if(tempAno[2] not in ano):
            ano.append(tempAno[2])

    for indice1 in ano:
        
        soma = 0.0
        for indice2 in concatena:
            
            temp = indice2.split("-")
            tempAno = temp[0].split("/")
            if(tempAno[2] == indice1):
                substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                soma += float(substituir)
            cont += 1
        cont = 0
        quantidades.append(soma)


    plt.bar(ano, quantidades, color="#228B22")
    plt.xticks(ano)
    plt.ylabel('Valores - R$')
    plt.xlabel('Ano')
    plt.title('Total de vendas por ano')
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

def page_settings(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Total de vendas por categoria:')
    #dados_vendas = pd.read_csv("Vendas2.csv")
    
    # letra B

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categoria = df['Categoria']
    categorias = ['Eletrodomésticos', 'Eletroportáteis', 'Eletrônicos', 'Celulares']
    cont = 0
    tamanhoDF = range(len(df))
    # df['Categoria'] = df['Categoria'].astype(str)

    # categorias = categoria.value_counts()
    quantidades = []

    # quantidades.append(categorias[0])
    # quantidades.append(categorias[1])
    # quantidades.append(categorias[2])
    # quantidades.append(categorias[3])


    for indice in categorias:
        
        soma = 0.0
        for indice2 in tamanhoDF:
            temp = df['Categoria'].iloc[indice2]
            if(temp == indice):
                substituir = df['ValorVenda'].iloc[indice2].replace(',', '.')
                soma += float(substituir)
                
        quantidades.append(soma)

    eixoX = ['Eletrodomêstico', 'Eletroportátel', 'Eletrônico', 'Celular']

    plt.bar(eixoX, quantidades, color="#ADD8E6")
    plt.xticks(eixoX)
    plt.ylabel('Valores - R$')
    plt.xlabel('Categorias')
    plt.title('Total de vendas por categoria')
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)
    

def page_dashboard2(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Total de vendas por categoria por ano:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categorias = []
    categoriasTotal = []
    ano = []
    dados = []
    listaTemp = []

    df['concatena'] = df.apply(lambda x: x['Categoria']+'-'+x['Data Venda'], axis=1)
    datavenda = df['Data Venda']

    for indice in datavenda:
        valor = indice.split("/")
        dados.append(valor)
        if(valor[2] not in ano):
            ano.append(valor[2])

    for indice in df['Categoria']:
        if(indice not in categorias):
            categorias.append(indice)
        
    for indice in ano:
        
        categoriasAno = []
        categoriasQuantidade = []
        somaCelulares = 0.0
        somaEletrodomesticos = 0.0
        somaEletronicos = 0.0
        somaEletroportateis = 0.0
        cont = 0
        
        for indice2 in df['concatena']:
            
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if(indice == temp2[2]):

                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelulares += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticos += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicos += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateis += float(substituir)
                categoriasAno.append(temp[0])
            cont += 1
        
        categoriasQuantidade.append(somaCelulares)
        categoriasQuantidade.append(somaEletrodomesticos)
        categoriasQuantidade.append(somaEletronicos)
        categoriasQuantidade.append(somaEletroportateis)
        
        categoriasTotal.append(categoriasQuantidade)          

    barWidth = 0.1

    plt.figure(figsize=(15,7))

    r1 = np.arange(len(categoriasTotal[0]))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]
    r6 = [x + barWidth for x in r5]

    plt.bar(r1, categoriasTotal[0], color='#1C1C1C', width=barWidth, label='2014')
    plt.bar(r2, categoriasTotal[1], color='#000080', width=barWidth, label='2015')
    plt.bar(r3, categoriasTotal[2], color='#ADD8E6', width=barWidth, label='2016')
    plt.bar(r4, categoriasTotal[3], color='#00FF7F', width=barWidth, label='2017')
    plt.bar(r5, categoriasTotal[4], color='#228B22', width=barWidth, label='2018')
    plt.bar(r6, categoriasTotal[5], color='#A020F0', width=barWidth, label='2019')

    plt.xlabel('Categorias')
    plt.xticks([r + barWidth for r in range(len(categoriasTotal[0]))], categorias)
    plt.ylabel('Valores - R$')
    plt.title('Quantidade total de vendas por categoria por ano')

    plt.legend()
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

def page_settings2(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Total de vendas por ano e categoria:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categorias = []
    categoriasTotal = []
    categoriasAno = []
    categoriasAnoTemp = []
    ano = []
    dados = []
    listaTemp = []

    df['concatena'] = df.apply(lambda x: x['Categoria']+'-'+x['Data Venda'], axis=1)
    datavenda = df['Data Venda']

    for indice in datavenda:
        valor = indice.split("/")
        dados.append(valor)
        if(valor[2] not in ano):
            ano.append(valor[2])

    for indice in df['Categoria']:
        if(indice not in categorias):
            categorias.append(indice)
            
    for indice in ano:
        
        categoriasAno = []
        categoriasQuantidade = []
        somaCelulares = 0.0
        somaEletrodomesticos = 0.0
        somaEletronicos = 0.0
        somaEletroportateis = 0.0
        cont = 0
        
        for indice2 in df['concatena']:
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if(indice == temp2[2]):

                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelulares += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticos += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicos += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateis += float(substituir)
                categoriasAno.append(temp[0])
            cont += 1
        
        categoriasQuantidade.append(somaCelulares)
        categoriasQuantidade.append(somaEletrodomesticos)
        categoriasQuantidade.append(somaEletronicos)
        categoriasQuantidade.append(somaEletroportateis)
        
        categoriasTotal.append(categoriasQuantidade)   
                
        
    #     for indice3 in categorias:
    #         categoriasQuantidade.append(categoriasAno.count(indice3))
        
    #     categoriasTotal.append(categoriasQuantidade)

    categoriasAno = []
    for indice in range(len(categoriasTotal[0])):
        categoriasAnoTemp = []
        for indice2 in range(len(categoriasTotal)):
            categoriasAnoTemp.append(categoriasTotal[indice2][indice])
        categoriasAno.append(categoriasAnoTemp)
            
    barWidth = 0.2

    plt.figure(figsize=(15,7))

    r1 = np.arange(len(ano))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    plt.bar(r1, categoriasAno[0], color='#1C1C1C', width=barWidth, label='Celulares')
    plt.bar(r2, categoriasAno[1], color='#000080', width=barWidth, label='Eletrodomesticos')
    plt.bar(r3, categoriasAno[2], color='#ADD8E6', width=barWidth, label='Eletrônicos')
    plt.bar(r4, categoriasAno[3], color='#00FF7F', width=barWidth, label='Eletroportáteis')

    plt.xlabel('Anos')
    plt.xticks([r + barWidth for r in range(len(ano))], ano)
    plt.ylabel('Valores  -  R$')
    plt.title('Quantidade total de vendas por ano e categoria')

    plt.legend()
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)
    

def page_dashboard3(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Total de vendas por categoria pelos meses para cada ano:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categorias = []
    categoriasTotalAno = []
    cont2 = 0
    ano = []
    dados = []
    listaTemp = []

    df['concatena'] = df.apply(lambda x: x['Categoria']+'-'+x['Data Venda'], axis=1)
    datavenda = df['Data Venda']

    for indice in datavenda:
        valor = indice.split("/")
        dados.append(valor)
        if(valor[2] not in ano):
            ano.append(valor[2])

    for indice in df['Categoria']:
        if(indice not in categorias):
            categorias.append(indice)
            
    for indice in ano:
    #     print("FOR 1")
        
        categoriasAno = []
        categoriasTotal = []
        categoriasQuantidadeJan = []
        categoriasQuantidadeFev = []
        categoriasQuantidadeMar = []
        categoriasQuantidadeAbr = []
        categoriasQuantidadeMai = []
        categoriasQuantidadeJun = []
        categoriasQuantidadeJul = []
        categoriasQuantidadeAgo = []
        categoriasQuantidadeSet = []
        categoriasQuantidadeOut = []
        categoriasQuantidadeNov = []
        categoriasQuantidadeDez = []
        
        somaCelularesJan = 0.0
        somaEletrodomesticosJan = 0.0
        somaEletronicosJan = 0.0
        somaEletroportateisJan = 0.0
        
        somaCelularesFev = 0.0
        somaEletrodomesticosFev = 0.0
        somaEletronicosFev = 0.0
        somaEletroportateisFev = 0.0
        
        somaCelularesMar = 0.0
        somaEletrodomesticosMar = 0.0
        somaEletronicosMar = 0.0
        somaEletroportateisMar = 0.0
        
        somaCelularesAbr = 0.0
        somaEletrodomesticosAbr = 0.0
        somaEletronicosAbr = 0.0
        somaEletroportateisAbr = 0.0
        
        somaCelularesMai = 0.0
        somaEletrodomesticosMai = 0.0
        somaEletronicosMai = 0.0
        somaEletroportateisMai = 0.0
        
        somaCelularesJun = 0.0
        somaEletrodomesticosJun = 0.0
        somaEletronicosJun = 0.0
        somaEletroportateisJun = 0.0
        
        somaCelularesJul = 0.0
        somaEletrodomesticosJul = 0.0
        somaEletronicosJul = 0.0
        somaEletroportateisJul = 0.0
        
        somaCelularesAgo = 0.0
        somaEletrodomesticosAgo = 0.0
        somaEletronicosAgo = 0.0
        somaEletroportateisAgo = 0.0
        
        somaCelularesSet = 0.0
        somaEletrodomesticosSet = 0.0
        somaEletronicosSet = 0.0
        somaEletroportateisSet = 0.0
        
        somaCelularesOut = 0.0
        somaEletrodomesticosOut = 0.0
        somaEletronicosOut = 0.0
        somaEletroportateisOut = 0.0
        
        somaCelularesNov = 0.0
        somaEletrodomesticosNov = 0.0
        somaEletronicosNov = 0.0
        somaEletroportateisNov = 0.0
        
        somaCelularesDez = 0.0
        somaEletrodomesticosDez = 0.0
        somaEletronicosDez = 0.0
        somaEletroportateisDez = 0.0
        cont = 0
        
        categoriasJan = []
        categoriasFev = []
        categoriasMar = []
        categoriasAbr = []
        categoriasMai = []
        categoriasJun = []
        categoriasJul = []
        categoriasAgo = []
        categoriasSet = []
        categoriasOut = []
        categoriasNov = []
        categoriasDez = []
        
        categoriasJanQt = []
        categoriasFevQt = []
        categoriasMarQt = []
        categoriasAbrQt = []
        categoriasMaiQt = []
        categoriasJunQt = []
        categoriasJulQt = []
        categoriasAgoQt = []
        categoriasSetQt = []
        categoriasOutQt = []
        categoriasNovQt = []
        categoriasDezQt = []
        
        for indice2 in df['concatena']:
    #         print("FOR 2")
            
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if((indice == temp2[2]) and (temp2[1] == '01')):
                
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesJan += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosJan += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosJan += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisJan += float(substituir)
                categoriasJan.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '02')):
    #             categoriasFev.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesFev += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosFev += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosFev += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisFev += float(substituir)
                categoriasFev.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '03')):
    #             categoriasMar.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesMar += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosMar += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosMar += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisMar += float(substituir)
                categoriasMar.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '04')):
    #             categoriasAbr.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesAbr += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosAbr += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosAbr += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisAbr += float(substituir)
                categoriasAbr.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '05')):
    #             categoriasMai.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesMai += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosMai += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosMai += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisMai += float(substituir)
                categoriasMai.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '06')):
    #             categoriasJun.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesJun += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosJun += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosJun += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisJun += float(substituir)
                categoriasJun.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '07')):
    #             categoriasJul.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesJul += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosJul += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosJul += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisJul += float(substituir)
                categoriasJul.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '08')):
    #             categoriasAgo.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesAgo += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosAgo += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosAgo += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisAgo += float(substituir)
                categoriasAgo.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '09')):
    #             categoriasSet.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesSet += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosSet += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosSet += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisSet += float(substituir)
                categoriasSet.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '10')):
    #             categoriasOut.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesOut += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosOut += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosOut += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisOut += float(substituir)
                categoriasOut.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '11')):
    #             categoriasNov.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesNov += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosNov += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosNov += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisNov += float(substituir)
                categoriasNov.append(temp[0])
                
            elif((indice == temp2[2]) and (temp2[1] == '12')):
    #             categoriasDez.append(temp[0])
                if(temp[0] == 'Celulares'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaCelularesDez += float(substituir)
                elif(temp[0] == 'Eletrodomésticos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletrodomesticosDez += float(substituir)
                elif(temp[0] == 'Eletrônicos'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletronicosDez += float(substituir)
                elif(temp[0] == 'Eletroportáteis'):
                    substituir = df['ValorVenda'].iloc[cont].replace(',', '.')
                    somaEletroportateisDez += float(substituir)
                categoriasDez.append(temp[0])
            cont += 1
            
        categoriasQuantidadeJan.append(somaCelularesJan)
        categoriasQuantidadeJan.append(somaEletrodomesticosJan)
        categoriasQuantidadeJan.append(somaEletronicosJan)
        categoriasQuantidadeJan.append(somaEletroportateisJan)

        categoriasQuantidadeFev.append(somaCelularesFev)
        categoriasQuantidadeFev.append(somaEletrodomesticosFev)
        categoriasQuantidadeFev.append(somaEletronicosFev)
        categoriasQuantidadeFev.append(somaEletroportateisFev)

        categoriasQuantidadeMar.append(somaCelularesMar)
        categoriasQuantidadeMar.append(somaEletrodomesticosMar)
        categoriasQuantidadeMar.append(somaEletronicosMar)
        categoriasQuantidadeMar.append(somaEletroportateisMar)

        categoriasQuantidadeAbr.append(somaCelularesAbr)
        categoriasQuantidadeAbr.append(somaEletrodomesticosAbr)
        categoriasQuantidadeAbr.append(somaEletronicosAbr)
        categoriasQuantidadeAbr.append(somaEletroportateisAbr)

        categoriasQuantidadeMai.append(somaCelularesMai)
        categoriasQuantidadeMai.append(somaEletrodomesticosMai)
        categoriasQuantidadeMai.append(somaEletronicosMai)
        categoriasQuantidadeMai.append(somaEletroportateisMai)

        categoriasQuantidadeJun.append(somaCelularesJun)
        categoriasQuantidadeJun.append(somaEletrodomesticosJun)
        categoriasQuantidadeJun.append(somaEletronicosJun)
        categoriasQuantidadeJun.append(somaEletroportateisJun)

        categoriasQuantidadeJul.append(somaCelularesJul)
        categoriasQuantidadeJul.append(somaEletrodomesticosJul)
        categoriasQuantidadeJul.append(somaEletronicosJul)
        categoriasQuantidadeJul.append(somaEletroportateisJul)

        categoriasQuantidadeAgo.append(somaCelularesAgo)
        categoriasQuantidadeAgo.append(somaEletrodomesticosAgo)
        categoriasQuantidadeAgo.append(somaEletronicosAgo)
        categoriasQuantidadeAgo.append(somaEletroportateisAgo)

        categoriasQuantidadeSet.append(somaCelularesSet)
        categoriasQuantidadeSet.append(somaEletrodomesticosSet)
        categoriasQuantidadeSet.append(somaEletronicosSet)
        categoriasQuantidadeSet.append(somaEletroportateisSet)

        categoriasQuantidadeOut.append(somaCelularesOut)
        categoriasQuantidadeOut.append(somaEletrodomesticosOut)
        categoriasQuantidadeOut.append(somaEletronicosOut)
        categoriasQuantidadeOut.append(somaEletroportateisOut)

        categoriasQuantidadeNov.append(somaCelularesNov)
        categoriasQuantidadeNov.append(somaEletrodomesticosNov)
        categoriasQuantidadeNov.append(somaEletronicosNov)
        categoriasQuantidadeNov.append(somaEletroportateisNov)

        categoriasQuantidadeDez.append(somaCelularesDez)
        categoriasQuantidadeDez.append(somaEletrodomesticosDez)
        categoriasQuantidadeDez.append(somaEletronicosDez)
        categoriasQuantidadeDez.append(somaEletroportateisDez)

        categoriasTotal.append(categoriasQuantidadeJan)
        categoriasTotal.append(categoriasQuantidadeFev)
        categoriasTotal.append(categoriasQuantidadeMar)
        categoriasTotal.append(categoriasQuantidadeAbr)
        categoriasTotal.append(categoriasQuantidadeMai)
        categoriasTotal.append(categoriasQuantidadeJun)
        categoriasTotal.append(categoriasQuantidadeJul)
        categoriasTotal.append(categoriasQuantidadeAgo)
        categoriasTotal.append(categoriasQuantidadeSet)
        categoriasTotal.append(categoriasQuantidadeOut)
        categoriasTotal.append(categoriasQuantidadeNov)
        categoriasTotal.append(categoriasQuantidadeDez)

        categoriasTotalAno.append(categoriasTotal)
        
    anoAtual = 2014
    # print(categoriasTotalAno)
    for indice in categoriasTotalAno:
    #     print(indice)
        barWidth = 0.05

        plt.figure(figsize=(25,17))

        r1 = np.arange(len(indice[0]))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        r4 = [x + barWidth for x in r3]
        r5 = [x + barWidth for x in r4]
        r6 = [x + barWidth for x in r5]
        r7 = [x + barWidth for x in r6]
        r8 = [x + barWidth for x in r7]
        r9 = [x + barWidth for x in r8]
        r10 = [x + barWidth for x in r9]
        r11 = [x + barWidth for x in r10]
        r12 = [x + barWidth for x in r11]
    #     print(indice)

        plt.bar(r1, indice[0], color='#1C1C1C', width=barWidth, label='Janeiro')
        plt.bar(r2, indice[1], color='#000080', width=barWidth, label='Fevereiro')
        plt.bar(r3, indice[2], color='#ADD8E6', width=barWidth, label='Março')
        plt.bar(r4, indice[3], color='#00FF7F', width=barWidth, label='Abril')
        plt.bar(r5, indice[4], color='#4682B4', width=barWidth, label='Maio')
        plt.bar(r6, indice[5], color='#006400', width=barWidth, label='Junho')
        plt.bar(r7, indice[6], color='#7CFC00', width=barWidth, label='Julho')
        plt.bar(r8, indice[7], color='#BDB76B', width=barWidth, label='Agosto')
        plt.bar(r9, indice[8], color='#A0522D', width=barWidth, label='Setembro')
        plt.bar(r10, indice[9], color='#FFDEAD', width=barWidth, label='Outubro')
        plt.bar(r11, indice[10], color='#4B0082', width=barWidth, label='Novembro')
        plt.bar(r12, indice[11], color='#800000', width=barWidth, label='Dezembro')

        plt.xlabel('Categorias')
        plt.xticks([r + barWidth for r in range(4)], ['Celulares', 'Eletrodomesticos', 'Eletronicos', 'Eletroportateis'])
        plt.ylabel('Valores - R$')
        plt.title('Total de vendas por categoria pelos meses para o ano de' + ' ' + str(anoAtual))

        plt.legend()
        plt.grid()
        fig = plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot(fig)
        anoAtual += 1

def page_settings3(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Produtos mais vendidos por cada fabricante:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    produtos = []
    fabricantes = []
    total = []

    df['concatena'] = df.apply(lambda x: x['Produto']+'-'+x['Fabricante'], axis=1)
    for indice in df['concatena']:
        
        valor = indice.split("-")

        for indice2 in valor:
            if(valor[1] not in fabricantes):
                fabricantes.append(valor[1])
        for indice3 in valor:
            if(valor[0] not in produtos):
                produtos.append(valor[0])

    for indice in fabricantes:
        produtosFabricante = []
        for indice2 in df['concatena']:
            
            valor = indice2.split("-")
    #         print(valor)
            if(indice == valor[1]):
                produtosFabricante.append(valor[0])
        total.append(produtosFabricante)

    # print(fabricantes)
    # 19 PRODUTOS
    # 16 FABRICANTES

    for indice in range(len(total)):
        tempDicio = {}
        for indice2 in produtos:
            quantidade = total[indice].count(indice2)
            tempDicio.update({indice2: quantidade})
    #         temp.append(total[indice].count(indice2))
    #     for item in sorted(tempDicio, key = tempDicio.get):
    #         print (tempDicio[item])
        sortedDict = sorted(tempDicio.items(), key=operator.itemgetter(1))
        dfFinal = DataFrame (sortedDict,columns=['Produto', 'Quantidade'])
        
        #   Desenhar o gráfico
        fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
        ax.vlines(x=dfFinal.index, ymin=0, ymax=dfFinal.Quantidade, color='firebrick', alpha=0.7, linewidth=20)
        
        for i, Quantidade in enumerate(dfFinal.Quantidade):
            ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

        # Title, Label, Ticks and Ylim
        ax.set_title(fabricantes[indice], fontdict={'size':22})
        ax.set(ylabel='Quantidades', ylim=(0, 480))
        plt.xticks(dfFinal.index, dfFinal.Produto.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

        # Add patches to color the X axis labels
        p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
        p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
        fig.add_artist(p1)
        fig.add_artist(p2)
        plotar = plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot(plotar)
    

def page_dashboard4(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Vendas das lojas por categoria:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categorias = []
    categoriasLojasTotal = []
    lojas = []
    # temp = []

    df['concatena'] = df.apply(lambda x: x['Categoria']+'-'+x['Loja'], axis=1)
    # datavenda = df['Data Venda']
    # print(df['concatena'])

    for indice in df['concatena']:
        valor = indice.split("-")
    #     temp.append(valor)
        if(valor[1] not in lojas):
            lojas.append(valor[1])
        if(valor[0] not in categorias):
            categorias.append(valor[0])

    for indice in lojas:
        
        categoriasLoja = []
        categoriasQuantidade = []
        
        for indice2 in df['concatena']:
            valor = indice2.split("-")
            if(indice == valor[1]):
                categoriasLoja.append(valor[0])
        
        for indice3 in categorias:
            categoriasQuantidade.append(categoriasLoja.count(indice3))
        
        categoriasLojasTotal.append(categoriasQuantidade)

    # print(categorias)
    # print(lojas)
    # print(categoriasLojasTotal)

    barWidth = 0.2

    plt.figure(figsize=(15,7))

    r1 = np.arange(len(categoriasLojasTotal[0]))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    # r5 = [x + barWidth for x in r4]
    # r6 = [x + barWidth for x in r5]
    # r7 = [x + barWidth for x in r6]


    plt.bar(r1, categoriasLojasTotal[0], color='#1C1C1C', width=barWidth, label='Celulares')
    plt.bar(r2, categoriasLojasTotal[1], color='#000080', width=barWidth, label='Eletrodomésticos')
    plt.bar(r3, categoriasLojasTotal[2], color='#ADD8E6', width=barWidth, label='Eletrônicos')
    plt.bar(r4, categoriasLojasTotal[3], color='#00FF7F', width=barWidth, label='Eletroportáteis')
    # plt.bar(r5, categoriasLojasTotal[4], color='#228B22', width=barWidth, label='AL1312')
    # plt.bar(r6, categoriasLojasTotal[5], color='#A020F0', width=barWidth, label='GA7751')
    # plt.bar(r7, categoriasLojasTotal[6], color='#00FF7F', width=barWidth, label='JB6325')

    plt.xlabel('\nR1296 = Recife  |  BA7783 = Salvador  |  JP8825 = João Pessoa  |  RG7742 = Natal  |  AL1312 = Maceió  |  GA7751 = Garanhuns  |  JB6325 = Jaboatão')
    plt.xticks([r + barWidth for r in range(len(categoriasLojasTotal))], lojas)
    plt.ylabel('Quantidade')
    plt.title('Vendas das lojas por categoria')

    plt.legend()
    plt.grid()
    plotar = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(plotar)

def page_settings4(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Ranking dos produtos com maiores vendas no geral e por loja:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    produtos = df['Produto'].tolist()
    lojas = df['Loja'].tolist()
    produtosTemp = []
    lojasTemp = []
    produtosQt = []
    produtosLista = []
    count = 0
        
    for indice in produtos:
        
        if(indice not in produtosTemp):
            produtosTemp.append(indice)
            
    for indice in lojas:
        
        if(indice not in lojasTemp):
            lojasTemp.append(indice)
        
    for indice2 in produtosTemp:
        produtosQt.append(produtos.count(indice2))
        
    dfProdutos = pd.DataFrame(list(zip(produtosTemp,produtosQt)), columns = ['Produtos','Quantidade'])
    dfProdutosOrdenados = dfProdutos.sort_values(by=['Quantidade'])

    # INICIO DE ÁREA PARA CRIAR O RANKING GERAL!

    #   Desenhar o gráfico
    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=dfProdutos.index, ymin=0, ymax=dfProdutosOrdenados.Quantidade, color='firebrick', alpha=0.7, linewidth=20)

    for i, Quantidade in enumerate(dfProdutosOrdenados.Quantidade):
        ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title('Geral', fontdict={'size':22})
    ax.set(ylabel='Quantidades', ylim=(0, 800))
    plt.xticks(dfProdutosOrdenados.index, dfProdutosOrdenados.Produtos.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

    # Add patches to color the X axis labels
    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)
    plt.show()

    # FIM DE ÁREA PARA CRIAR O RANKING GERAL!

    print('         19º  18º   17º   16º  15º   14º  13º  12º   11º  10º   9º    8º   7º    6º   5º   4º    3º   2º    1º')
    print('\n')
    print('\n')

    df['concatena'] = df.apply(lambda x: x['Produto']+'-'+x['Loja'], axis=1)
    tempProdutosLoja = []

    # print(lojasTemp)

    for indice in lojasTemp:
        
        temp = []
        
        for indice2 in df['concatena']:
            valor = indice2.split("-")
            if(valor[1] == indice):
                temp.append(valor[0])
                
        tempProdutosLoja.append(temp)
        
    for indice3 in tempProdutosLoja:

        produtosLojaQuantidade = []
        for indice4 in produtosTemp:
            produtosLojaQuantidade.append(indice3.count(indice4))

        dfProdutos = pd.DataFrame(list(zip(produtosTemp,produtosLojaQuantidade)), columns = ['Produtos','Quantidade'])
        dfProdutosOrdenados = dfProdutos.sort_values(by=['Quantidade'])

        # INICIO DE ÁREA PARA CRIAR O RANKING GERAL POR LOJA!

        #   Desenhar o gráfico
        fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
        ax.vlines(x=dfProdutos.index, ymin=0, ymax=dfProdutosOrdenados.Quantidade, color='firebrick', alpha=0.7, linewidth=20)

        for i, Quantidade in enumerate(dfProdutosOrdenados.Quantidade):
            ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

        # Title, Label, Ticks and Ylim
        ax.set_title(lojasTemp[count], fontdict={'size':22})
        ax.set(ylabel='Quantidades', ylim=(0, 800))
        plt.xticks(dfProdutosOrdenados.index, dfProdutosOrdenados.Produtos.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

        # Add patches to color the X axis labels
        p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
        p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
        fig.add_artist(p1)
        fig.add_artist(p2)
        plotar = plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot(plotar)
        
        count += 1

        # FIM DE ÁREA PARA CRIAR O RANKING GERAL!
        print('         19º  18º   17º   16º  15º   14º  13º  12º   11º  10º   9º   8º   7º    6º   5º   4º    3º   2º    1º')
        print('\n')
        print('\n')
    

def page_dashboard5(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Ranking dos produtos com menores vendas no geral e por loja:')

    # letra I

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    produtos = df['Produto'].tolist()
    lojas = df['Loja'].tolist()
    produtosTemp = []
    lojasTemp = []
    produtosQt = []
    produtosLista = []
    count = 0
        
    for indice in produtos:
        
        if(indice not in produtosTemp):
            produtosTemp.append(indice)
            
    for indice in lojas:
        
        if(indice not in lojasTemp):
            lojasTemp.append(indice)
        
    for indice2 in produtosTemp:
        produtosQt.append(produtos.count(indice2))
        
    dfProdutos = pd.DataFrame(list(zip(produtosTemp,produtosQt)), columns = ['Produtos','Quantidade'])
    dfProdutosOrdenados = dfProdutos.sort_values(by=['Quantidade'], ascending=False)

    # print(dfProdutos)
    # print(dfProdutosOrdenados)

    # INICIO DE ÁREA PARA CRIAR O RANKING GERAL!

    #   Desenhar o gráfico
    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=dfProdutos.index, ymin=0, ymax=dfProdutosOrdenados.Quantidade, color='firebrick', alpha=0.7, linewidth=20)

    for i, Quantidade in enumerate(dfProdutosOrdenados.Quantidade):
        ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title('Geral', fontdict={'size':22})
    ax.set(ylabel='Quantidades', ylim=(0, 800))
    plt.xticks(dfProdutosOrdenados.index, dfProdutosOrdenados.Produtos.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

    # Add patches to color the X axis labels
    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)
    plt.show()

    # FIM DE ÁREA PARA CRIAR O RANKING GERAL!

    print('         19º  18º   17º   16º  15º   14º  13º  12º   11º  10º   9º    8º   7º   6º    5º   4º   3º   2º    1º')
    print('\n')
    print('\n')

    df['concatena'] = df.apply(lambda x: x['Produto']+'-'+x['Loja'], axis=1)
    tempProdutosLoja = []

    # print(lojasTemp)

    for indice in lojasTemp:
        
        temp = []
        
        for indice2 in df['concatena']:
            valor = indice2.split("-")
            if(valor[1] == indice):
                temp.append(valor[0])
                
        tempProdutosLoja.append(temp)
        
    for indice3 in tempProdutosLoja:

        produtosLojaQuantidade = []
        for indice4 in produtosTemp:
            produtosLojaQuantidade.append(indice3.count(indice4))

        dfProdutos = pd.DataFrame(list(zip(produtosTemp,produtosLojaQuantidade)), columns = ['Produtos','Quantidade'])
        dfProdutosOrdenados = dfProdutos.sort_values(by=['Quantidade'], ascending=False)

        # INICIO DE ÁREA PARA CRIAR O RANKING GERAL POR LOJA!

        #   Desenhar o gráfico
        fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
        ax.vlines(x=dfProdutos.index, ymin=0, ymax=dfProdutosOrdenados.Quantidade, color='firebrick', alpha=0.7, linewidth=20)

        for i, Quantidade in enumerate(dfProdutosOrdenados.Quantidade):
            ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

        # Title, Label, Ticks and Ylim
        ax.set_title(lojasTemp[count], fontdict={'size':22})
        ax.set(ylabel='Quantidades', ylim=(0, 800))
        plt.xticks(dfProdutosOrdenados.index, dfProdutosOrdenados.Produtos.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

        # Add patches to color the X axis labels
        p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
        p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
        fig.add_artist(p1)
        fig.add_artist(p2)
        plotar = plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot(plotar)
        
        count += 1

        # FIM DE ÁREA PARA CRIAR O RANKING GERAL!
        print('         19º  18º   17º   16º  15º   14º  13º  12º   11º  10º   9º   8º   7º    6º   5º   4º    3º   2º    1º')
        print('\n')
        print('\n')

def page_settings5(state):
    
    st.markdown("<h1 style='text-align: center;'>Ciência de Dados</h1>", unsafe_allow_html=True)
    st.header('Ranking de vendas por lojas:')

    # letra K

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    produtos = df['Produto'].tolist()
    lojas = df['Loja'].tolist()
    ranking = []
    lojasTemp = []

    for indice in lojas:
        if(indice not in lojasTemp):
            lojasTemp.append(indice)
        

    for indice in lojasTemp:
        ranking.append(lojas.count(indice))

    # print(lojasTemp)
    # print(ranking)

    dfLojas = pd.DataFrame(list(zip(lojasTemp,ranking)), columns = ['Lojas','Quantidade'])
    dfLojasOrdenados = dfLojas.sort_values(by=['Quantidade'], ascending=True)
    # print(dfLojas)



    # INICIO DE ÁREA PARA CRIAR O RANKING DE VENDAS POR LOJA!

    #   Desenhar o gráfico
    fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
    ax.vlines(x=dfLojas.index, ymin=0, ymax=dfLojasOrdenados.Quantidade, color='firebrick', alpha=0.7, linewidth=20)

    for i, Quantidade in enumerate(dfLojasOrdenados.Quantidade):
        ax.text(i, Quantidade+0.5, round(Quantidade, 1), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title('Ranking de Vendas por Loja', fontdict={'size':22})
    ax.set(ylabel='Quantidades', ylim=(0, 1800))
    plt.xticks(dfLojas.index, dfLojasOrdenados.Lojas.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

    # Add patches to color the X axis labels
    p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
    p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
    fig.add_artist(p1)
    fig.add_artist(p2)
    plotar = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(plotar)

    # FIM DE ÁREA PARA CRIAR O RANKING DE VENDAS POR LOJA!
    print('          7º               6º              5º              4º               3º              2º              1º')
    print('\n')
    print('\n')
    




# PARA REMOVER DEPOIS!

def display_state_values(state):
    st.write("Input state:", state.input)
    st.write("Slider state:", state.slider)
    st.write("Radio state:", state.radio)
    st.write("Checkbox state:", state.checkbox)
    st.write("Selectbox state:", state.selectbox)
    st.write("Multiselect state:", state.multiselect)
    
    for i in range(3):
        st.write(f"Value {i}:", state[f"State value {i}"])

    if st.button("Clear state"):
        state.clear()

class _SessionState:

    def __init__(self, session, hash_funcs):
        """Initialize SessionState instance."""
        self.__dict__["_state"] = {
            "data": {},
            "hash": None,
            "hasher": _CodeHasher(hash_funcs),
            "is_rerun": False,
            "session": session,
        }

    def __call__(self, **kwargs):
        """Initialize state data once."""
        for item, value in kwargs.items():
            if item not in self._state["data"]:
                self._state["data"][item] = value

    def __getitem__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)
        
    def __getattr__(self, item):
        """Return a saved state value, None if item is undefined."""
        return self._state["data"].get(item, None)

    def __setitem__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value

    def __setattr__(self, item, value):
        """Set state value."""
        self._state["data"][item] = value
    
    def clear(self):
        """Clear session state and request a rerun."""
        self._state["data"].clear()
        self._state["session"].request_rerun()
    
    def sync(self):
        """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

        # Ensure to rerun only once to avoid infinite loops
        # caused by a constantly changing state value at each run.
        #
        # Example: state.value += 1
        if self._state["is_rerun"]:
            self._state["is_rerun"] = False
        
        elif self._state["hash"] is not None:
            if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                self._state["is_rerun"] = True
                self._state["session"].request_rerun()

        self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)

def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    
    return session_info.session


def _get_state(hash_funcs=None):
    session = _get_session()

    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = _SessionState(session, hash_funcs)

    return session._custom_session_state

if __name__ == "__main__":
    main()

####################################################################################################