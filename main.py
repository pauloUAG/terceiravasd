import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import operator
from pandas import DataFrame
import matplotlib.patches as patches
from streamlit.hashing import _CodeHasher
import datetime
from datetime import date
import statistics
#%matplotlib inline

st.title("Ciência de Dados - 3º VA")

my_form = st.form(key = "form1")
date = my_form.date_input('Data', date.today())
data = str(date)
submit = my_form.form_submit_button(label = "Enviar")
col1,col2,col3,col4,col5,col6 = st.beta_columns([1,2,3,4,5,6])
listaData = []
listaEstado = []
listaCasoAcumulado = []
listaMediaMovelCasoAtual = []
listaMediaMovelCasoAnterior = []
listaSituacaoCasos = []
listaPercentualCasos = []
listaObitosAcumulados = []
listaMediaMovelObitosAtual = []
listaMediaMovelObitosAnterior = []
listaSituacaoObitos = []
listaPercentualObitos = []
#st.write(date)

#url1 = "C:\Users\sousa\OneDrive\Documentos\HIST_PAINEL_COVIDBR_11jul2021\HIST_PAINEL_COVIDBR_2021_Parte1_11jul2021.csv"
#url2 = "C:\Users\sousa\OneDrive\Documentos\HIST_PAINEL_COVIDBR_11jul2021\HIST_PAINEL_COVIDBR_2021_Parte2_11jul2021.csv"
#df1 = pd.read_csv(r"HIST_PAINEL_COVIDBR_2020_Parte1_11jul2021.csv", sep = ';')
#df2 = pd.read_csv(r"HIST_PAINEL_COVIDBR_2020_Parte2_11jul2021.csv", sep = ';')
df1 = pd.read_csv(r"HIST_PAINEL_COVIDBR_2021_Parte1_11jul2021.csv", sep = ';')
df2 = pd.read_csv(r"HIST_PAINEL_COVIDBR_2021_Parte2_11jul2021.csv", sep = ';')
listFrames = [df1, df2]

resultedFrame = pd.concat(listFrames)

temp = resultedFrame.loc[resultedFrame['data'] == data]
#print(temp)

if(len(temp) == 0):
    st.write("A data especifícada não foi encontrada nos nossos registros!")

else:

    for indice in temp.index:
    
        situacaoCasos = ""
        listaMediaAtual = []
        listaMediaAnterior = []
        listaMediaObitosAtual = []
        listaMediaObitosAnterior = []
        porcentagemCasos = 0.0

        estado = resultedFrame['estado'].iloc[indice]
        casosAcumulado = resultedFrame['casosAcumulado'].iloc[indice]
        obitosAcumulado = resultedFrame['obitosAcumulado'].iloc[indice]

        temp1 = float(resultedFrame['casosNovos'].iloc[indice])
        temp2 = float(resultedFrame['casosNovos'].iloc[indice-1])
        temp3 = float(resultedFrame['casosNovos'].iloc[indice-2])
        temp4 = float(resultedFrame['casosNovos'].iloc[indice-3])
        temp5 = float(resultedFrame['casosNovos'].iloc[indice-4])
        temp6 = float(resultedFrame['casosNovos'].iloc[indice-5])
        temp7 = float(resultedFrame['casosNovos'].iloc[indice-6])
        temp8 = float(resultedFrame['casosNovos'].iloc[indice-7])

        temp9 = float(resultedFrame['obitosNovos'].iloc[indice])
        temp10 = float(resultedFrame['obitosNovos'].iloc[indice-1])
        temp11 = float(resultedFrame['obitosNovos'].iloc[indice-2])
        temp12 = float(resultedFrame['obitosNovos'].iloc[indice-3])
        temp13 = float(resultedFrame['obitosNovos'].iloc[indice-4])
        temp14 = float(resultedFrame['obitosNovos'].iloc[indice-5])
        temp15 = float(resultedFrame['obitosNovos'].iloc[indice-6])
        temp16 = float(resultedFrame['obitosNovos'].iloc[indice-7])

        listaMediaAtual.append(abs(temp1))
        listaMediaAtual.append(abs(temp2))
        listaMediaAtual.append(abs(temp3))
        listaMediaAtual.append(abs(temp4))
        listaMediaAtual.append(abs(temp5))
        listaMediaAtual.append(abs(temp6))
        listaMediaAtual.append(abs(temp7))

        #print(listaMediaAtual)

        listaMediaAnterior.append(abs(temp2))
        listaMediaAnterior.append(abs(temp3))
        listaMediaAnterior.append(abs(temp4))
        listaMediaAnterior.append(abs(temp5))
        listaMediaAnterior.append(abs(temp6))
        listaMediaAnterior.append(abs(temp7))
        listaMediaAnterior.append(abs(temp8))

        listaMediaObitosAtual.append(abs(temp9))
        listaMediaObitosAtual.append(abs(temp10))
        listaMediaObitosAtual.append(abs(temp11))
        listaMediaObitosAtual.append(abs(temp12))
        listaMediaObitosAtual.append(abs(temp13))
        listaMediaObitosAtual.append(abs(temp14))
        listaMediaObitosAtual.append(abs(temp15))

        listaMediaObitosAnterior.append(abs(temp10))
        listaMediaObitosAnterior.append(abs(temp11))
        listaMediaObitosAnterior.append(abs(temp12))
        listaMediaObitosAnterior.append(abs(temp13))
        listaMediaObitosAnterior.append(abs(temp14))
        listaMediaObitosAnterior.append(abs(temp15))
        listaMediaObitosAnterior.append(abs(temp16))

        media1 = statistics.mean(listaMediaAtual)
        media2 = statistics.mean(listaMediaAnterior)
        mediaAtual = round(media1)
        mediaAnterior = round(media2)
        #print(mediaAtual)

        media3 = statistics.mean(listaMediaObitosAtual)
        media4 = statistics.mean(listaMediaObitosAnterior)
        mediaObitosAtual = round(media3)
        mediaObitosAnterior = round(media4)
        
        if(mediaAtual == 0.0 and mediaAnterior == 0.0):
            situacao = "Estabilidade"
            porcentagemCasos = 0
        elif(mediaAtual == 0.0 and mediaAnterior != 0.0):
            situacao = "Baixa"
            porcentagemCasos = 100
        elif(mediaAnterior == 0.0 and mediaAtual != 0.0):
            situacao = "Aumento"
            porcentagemCasos = 100
        else:
            if(mediaAtual > mediaAnterior):
                situacao = "Aumento"
                porcentagemCasos = round(abs((((mediaAtual - mediaAnterior)/mediaAnterior) * 100)))
            elif(mediaAtual < mediaAnterior):
                situacao = "Baixa"
                porcentagemCasos = round(abs((((mediaAtual - mediaAnterior)/mediaAtual) * 100)))
            else:
                situacao = "Estabilidade"
                
        if(mediaObitosAtual == 0.0 and mediaObitosAnterior == 0.0):
            situacaoObitos = "Estabilidade"
            porcentagemObitos = 0
        elif(mediaObitosAtual == 0.0 and mediaObitosAnterior != 0.0):
            situacaoObitos = "Baixa"
            porcentagemObitos = 100
        elif(mediaObitosAnterior == 0.0 and mediaObitosAtual != 0.0):
            situacaoObitos = "Aumento"
            porcentagemObitos = 100
        else:
            if(mediaObitosAtual > mediaObitosAnterior):
                situacaoObitos = "Aumento"
                porcentagemObitos = round(abs((((mediaObitosAtual - mediaObitosAnterior)/mediaObitosAnterior) * 100)))
            elif(mediaObitosAtual < mediaObitosAnterior):
                situacaoObitos = "Baixa"
                porcentagemObitos = round(abs((((mediaObitosAtual - mediaObitosAnterior)/mediaObitosAtual) * 100)))
            else:
                situacaoObitos = "Estabilidade"

        listaData.append(data)
        listaEstado.append(estado)
        listaCasoAcumulado.append(casosAcumulado)
        listaMediaMovelCasoAtual.append(mediaAtual)
        listaMediaMovelCasoAnterior.append(mediaAnterior)
        listaSituacaoCasos.append(situacao)
        listaPercentualCasos.append(porcentagemCasos)
        listaObitosAcumulados.append(obitosAcumulado)
        listaMediaMovelObitosAtual.append(mediaObitosAtual)
        listaMediaMovelObitosAnterior.append(mediaObitosAnterior)
        listaSituacaoObitos.append(situacaoObitos)
        listaPercentualObitos.append(porcentagemObitos)
        #print(listaMediaMovelCasoAtual)

    dataFrame = {'Data': listaData,
                'Estado': listaEstado,
                'Casos Acumulados': listaCasoAcumulado,
                'Média Móvel Atual': listaMediaMovelCasoAtual,
                'Média Móvel Anterior': listaMediaMovelCasoAnterior,
                'Situação Atual': listaSituacaoCasos,
                '% Percentual Casos Atual': listaPercentualCasos,
                'Óbitos Acumulados': listaObitosAcumulados,
                'Média Móvel Atual Óbitos': listaMediaMovelObitosAtual,
                'Média Móvel Anterior Óbitos': listaMediaMovelObitosAnterior,
                'Situação Óbitos Atual': listaSituacaoObitos,
                '% Percentual Óbitos Atual': listaPercentualObitos}

    st.dataframe(dataFrame)
#print(dataFrame)