import os, openpyxl
from openpyxl.styles import Alignment 
import matplotlib.pyplot as plt
import pandas as pd

planilha = openpyxl.Workbook ()

page = planilha ['Sheet']
page.title = "DADOS DO COVID"

page = planilha.active

# Adicionando dados

page['A1'].value = "Data" 
page['B1'].value = "Novos casos" 
page['C1'].value = "Mortes" 

page['A2'].value = "20/02" 
page['B2'].value = "57472" 
page['C2'].value = "1212" 

page['A3'].value = "21/02" 
page['B3'].value = "29026" 
page['C3'].value = "527" 

page['A4'].value = "22/02" 
page['B4'].value = "26986" 
page['C4'].value = "639"

page['A5'].value = "23/02"
page['B5'].value = "62715"
page['C5'].value = "1386"

page['A6'].value = "24/02"
page['B6'].value = "66588"
page['C6'].value = "1428"

page['A7'].value = "25/02"
page['B7'].value = "65998"
page['C7'].value = "1541"

page['A8'].value = "26/02"
page['B8'].value = "65169"
page['C8'].value = "1337"

page['A9'].value = "27/02"
page['B9'].value = "61602"
page['C9'].value = "1386"


planilha.save ("dados-morte.xlsx")


#CRIANDO GRÁFICO

planilha = pd.read_excel ("dados-morte.xlsx")

dia = planilha ['Data']
casos = planilha ['Novos casos']
mortes = planilha ['Mortes']


print ("Gerando os gráficos")
plt.title ("Casos novos de covid por data de notificação no Brasil - 20/02 a 27/02")
plt.bar (dia, mortes, color = 'orange', width = 0.5)
plt.savefig ("novos.png")



print ("Gerando os gráficos")
plt.title ("Mortes de covid por data de notificação no Brasil - 20/02 a 27/02")
plt.bar (dia, mortes, color = 'red', width = 0.5)
plt.savefig ("mortes.png")

#criando planilha

planilha = openpyxl.Workbook ()

page = planilha ['Sheet']
page.title = "DADOS"

page = planilha.active

page['A1'].value = "Pessoas" 
page['B1'].value = "Porcentagem"   

page['A2'].value = "Entrevistados" 
page['B2'].value = "1.996" 

page['A3'].value = "Mais ansiosos" 
page['B3'].value = "1.597"  
  

planilha.save ("grafico-casos.xlsx")

#criando gráfico

planilha = pd.read_excel("grafico-casos.xlsx")

pessoas = planilha['Pessoas']
porc = planilha['Porcentagem']

plt.title("Pessoas entrevistadas sobre o aumento da ansiedade - UFRGS 2020")

plt.pie(porc, labels=pessoas,  autopct='%1.0f%%')
plt.savefig("ansiosos.png")
# fonte: https://covid.saude.gov.br

#grafico homem e mulher
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

plt.savefig("homem-mulher.png")

os.system ("pause")

