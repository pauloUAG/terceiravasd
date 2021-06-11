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


with header:
    st.title('Fundamentos em Ciência de Dados')
    st.markdown(""" """)

st.sidebar.markdown("## Select Data Time and Detector")
#st.sidebar.selectbox("Selecione um número", [1,2,3])


with dataset:

    st.header('1º Gráfico:')
    #dados_vendas = pd.read_csv("Vendas2.csv")
    
    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    datavenda = df['Data Venda']
    ano = []
    dados = []
    quantidades = []


    for indice in datavenda:
        valor = indice.split("/")
        dados.append(valor)
        if(valor[2] not in ano):
            ano.append(valor[2])
            
    for indice1 in ano:
        cont = 0
        for indice2 in datavenda:
            temp = indice2.split("/")
            if(temp[2] == indice1):
                cont += 1
        quantidades.append(cont)


    plt.bar(ano, quantidades, color="#228B22")
    plt.xticks(ano)
    plt.ylabel('Quantidade')
    plt.xlabel('Ano')
    plt.title('Total de vendas por ano')
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

    ###########################################################################################################################

    st.header('2º Gráfico:')
    #dados_vendas = pd.read_csv("Vendas2.csv")
    
    # letra B

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categoria = df['Categoria']

    categorias = categoria.value_counts()
    quantidades = []
    quantidades.append(categorias[0])
    quantidades.append(categorias[1])
    quantidades.append(categorias[2])
    quantidades.append(categorias[3])

    eixoX = ['Eletrodomêstico', 'Eletroportátel', 'Eletrônico', 'Celular']

    plt.bar(eixoX, quantidades, color="#ADD8E6")
    plt.xticks(eixoX)
    plt.ylabel('Quantidade')
    plt.xlabel('Categorias')
    plt.title('Total de vendas por categoria')
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

    ###########################################################################################################################

    st.header('3º Gráfico:')

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
        
        for indice2 in df['concatena']:
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if(indice == temp2[2]):
                categoriasAno.append(temp[0])
                
        
        for indice3 in categorias:
            categoriasQuantidade.append(categoriasAno.count(indice3))
        
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
    plt.ylabel('Quantidade')
    plt.title('Quantidade total de vendas por categoria por ano')

    plt.legend()
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

    ###########################################################################################################################

    st.header('4º Gráfico:')

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
        
        for indice2 in df['concatena']:
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if(indice == temp2[2]):
                categoriasAno.append(temp[0])
                
        
        for indice3 in categorias:
            categoriasQuantidade.append(categoriasAno.count(indice3))
        
        categoriasTotal.append(categoriasQuantidade)

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
    plt.ylabel('Quantidade')
    plt.title('Quantidade total de vendas por ano e categoria')

    plt.legend()
    plt.grid()
    fig = plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot(fig)

    ###########################################################################################################################

    st.header('5º Gráfico:')

    url = 'Vendas.csv'
    df = pd.read_csv(url, encoding = 'cp1252', sep = ';')
    categorias = []
    categoriasTotalAno = []
    # categoriasAnoTemp = []
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
        categoriasTotal = []
        
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
            temp = indice2.split("-")
            temp2 = temp[1].split("/")

            if((indice == temp2[2]) and (temp2[1] == '01')):
                categoriasJan.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '02')):
                categoriasFev.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '03')):
                categoriasMar.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '04')):
                categoriasAbr.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '05')):
                categoriasMai.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '06')):
                categoriasJun.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '07')):
                categoriasJul.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '08')):
                categoriasAgo.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '09')):
                categoriasSet.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '10')):
                categoriasOut.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '11')):
                categoriasNov.append(temp[0])
            elif((indice == temp2[2]) and (temp2[1] == '12')):
                categoriasDez.append(temp[0])
        
        for indice3 in categorias:
            categoriasJanQt.append(categoriasJan.count(indice3))
            categoriasFevQt.append(categoriasFev.count(indice3))
            categoriasMarQt.append(categoriasMar.count(indice3))
            categoriasAbrQt.append(categoriasAbr.count(indice3))
            categoriasMaiQt.append(categoriasMai.count(indice3))
            categoriasJunQt.append(categoriasJun.count(indice3))
            categoriasJulQt.append(categoriasJul.count(indice3))
            categoriasAgoQt.append(categoriasAgo.count(indice3))
            categoriasSetQt.append(categoriasSet.count(indice3))
            categoriasOutQt.append(categoriasOut.count(indice3))
            categoriasNovQt.append(categoriasNov.count(indice3))
            categoriasDezQt.append(categoriasDez.count(indice3))
        
    #     print(categoriasDezQt)
        categoriasTotal.append(categoriasJanQt)
        categoriasTotal.append(categoriasFevQt)
        categoriasTotal.append(categoriasMarQt)
        categoriasTotal.append(categoriasAbrQt)
        categoriasTotal.append(categoriasMaiQt)
        categoriasTotal.append(categoriasJunQt)
        categoriasTotal.append(categoriasJulQt)
        categoriasTotal.append(categoriasAgoQt)
        categoriasTotal.append(categoriasSetQt)
        categoriasTotal.append(categoriasOutQt)
        categoriasTotal.append(categoriasNovQt)
        categoriasTotal.append(categoriasDezQt)
        
        categoriasTotalAno.append(categoriasTotal)

    categoriasAno = []
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
        plt.ylabel('Quantidade')
        plt.title('Total de vendas por categoria pelos meses para o ano de' + ' ' + str(anoAtual))

        plt.legend()
        plt.grid()
        fig = plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot(fig)
        anoAtual += 1

    ###########################################################################################################################

    st.header('6º Gráfico:')

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

    ###########################################################################################################################

    st.header('7º Gráfico:')

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

    ###########################################################################################################################

    st.header('8º Gráfico:')

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

    ###########################################################################################################################

    st.header('9º Gráfico:')

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

    ###########################################################################################################################

    st.header('10º Gráfico:')

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

    ###########################################################################################################################