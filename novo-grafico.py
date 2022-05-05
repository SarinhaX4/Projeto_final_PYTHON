import os
from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl 

planilha = openpyxl.Workbook ()

page = planilha ['Sheet']
page.title = "DADOS"

page = planilha.active

page['A1'].value = "Pessoas" 
page['B1'].value = "Porcentagem"   

page['A2'].value = "Mulheres" 
page['B2'].value = "1000" 

page['A3'].value = "Homens" 
page['B3'].value = "500" 


planilha.save ("grafico-homem-mulher.xlsx")

#criando gráfico
planilha = pd.read_excel("grafico-homem-mulher.xlsx")

pessoas = planilha['Pessoas']
porc = planilha['Porcentagem']

plt.title("Pessoas entrevistadas sobre o aumento da ansiedade - UFRGS 2020")

plt.pie(porc, labels=pessoas,  autopct='%1.0f%%')

plt.show()



