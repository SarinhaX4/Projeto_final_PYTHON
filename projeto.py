import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Capa 
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.set_font('Times', 'B',18)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 40, 'O aumento de casos de ansiedade e depressão ', align='C', ln=1)
pdf.cell(0, 0, 'durante a pandemia do COVID19', align='C', ln=1)

pdf.set_font('Times', '', 20)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 227, 'Sara Cristina', align='C', ln=1)

pdf.set_font('Times', '', 15)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 0, 'Turma D', align='C', ln=1)

# Gerando PDF:

#Conteudo do relatorio
page1 = "INTRODUÇÃO\n\nO presente relátório discorrerá sobre os impactos na saúde mental, que a pandemia do SAS COV 19 trouxe á população. Mais concretamente, sobre como a ansiedade atigiu as pessoas, qual a faixa etária predominante, quais consequencias ela trouxe a vida pessoal das pessoas, e como o governo brasileiro vem ajudando a tratar. \nÉ objetivo deste relatório mostrar que a problemática é real e atual no Brasil.\n\nPORQUÊ A ANSIEDADE ESTEVE PRESENTE\n\nA mudança brusca de rotina que a pandemia causou na vida e no trabalho das pessoas trouxe impactos também para a saúde mental.\nÉ o que mostra um estudo realizado pela Universidade do Estado do Rio de Janeiro (UERJ) e publicado pela revista The Lancet. De acordo com o artigo, os casos de depressão aumentaram 90% e o número de pessoas que relataram sintomas como crise de ansiedade e estresse agudo mais que dobrou entre os meses de março e abril deste ano.\n Os problemas de saúde mental no trabalho estão ligados a três pilares: tempo, espaço e condições. A afirmação foi feita pela diretora da Fiocruz Brasília, Fabiana Damásio. Para ela, ao analisar o tempo, percebe-se uma ausência de limites entre trabalho e vida pessoal e o entrecruzamento do trabalho com as atividades domésticas. A psicóloga lembrou que as questões das desigualdades sociais eclodem neste momento quando nos deparamos com a pandemia, em que os espaços físicos foram transferidos para redes comunicacionais como mídias sociais, plataformas virtuais e tecnologias para garantir que essas redes permaneçam.\nAlém disso, a incerteza sobre o futuro e a quantidade de mortes todos os dias, trazia a sociedade uma insegurança sobre o que esperar do amanhã.\n\nConfira um gráfico que retrata a quantidade a quantidade de novos casos e também a quantidade de mortes por dia. \n"
pdf.add_page()
pdf.set_font('Times','',14)
pdf.multi_cell(w=0, h=7, txt= page1, align='J')
pdf.image("novos.png", x=40, y= 210, w= 110)

pdf.add_page()
page2 = "Coordenada pela professora Adriane Ribeiro Rosa, a pesquisa Covid-19 Saúde mental: usando a tecnologia digital para avaliação das consequências da pandemia, realizada por um grupo multidisciplinar de pesquisadores do Laboratório de Psiquiatria Molecular da UFRGS e do Hospital de Clínicas de Porto Alegre, é o primeiro estudo brasileiro publicado em revista internacional (COVID-19 and mental health in Brazil: Psychiatric symptoms in the general population) mostrando que cerca de 80(porcento) da população sente-se mais ansiosa, 68(porcento) têm sintomas depressivos, 65(porcento)  expressam sentimentos de raiva, 63(porcento) apresentam sintomas somáticos e cerca de 50(porcento) relatam alterações no sono.\nConforme Adriane, o objetivo do estudo foi identificar a prevalência de sintomas psiquiátricos e os fatores associados a ela na população brasileira. Para isso, foi realizada pesquisa online entre os dias 20 de maio e 14 de julho, amplamente divulgada nas redes sociais, que teve a participação de 1.996 indivíduos. Os participantes responderam a um questionário que avaliou a presença de 13 tipos diferentes de transtornos psiquiátricos, a gravidade dos sintomas apresentados e outras variáveis de interesse, tais como: informações sociodemográficas; histórico de doenças médicas e psiquiátricas; grau de conhecimento sobre a covid-19; atitudes e práticas de higiene; grau de funcionalidade durante a pandemia; e qualidade de vida.\n\n"
pdf.multi_cell(w=0, h=7, txt=page2, align='J')
pdf.image("ansiosos..png", x=10, y= 140, w= 190)

pdf.add_page()
page3 = "As mulheres são as mais afetadas\n\n“Embora a pesquisa não tenha detalhado as razões que levaram as mulheres a terem maior sofrimento psíquico, a literatura médica vem mostrando que são elas que têm maiores impactos pelas condições sociais em que vivem. A pandemia só acirrou essa situação”, diz o neuropsicólogo. Elas cumprem dupla jornada, acompanham o desenvolvimento escolar dos filhos e, na pandemia, mais pessoas permaneceram dentro de casa, além das preocupações relacionadas ao próprio vírus (iminência de contaminação, necessidade de mudanças de hábitos de higiene, redução de convívio social, familiares adoecidos, etc.). “Todas essas circunstâncias geram estresse e podem ser gatilhos detonadores de doenças mentais”, explica o professor Pádua Serafim."
pdf.multi_cell(w=0, h=7, txt=page2, align='J')
pdf.image("homem_mulher.png", x=5, y= 180, w= 190)

pdf.output("projeto.pdf")

os.system("pause")