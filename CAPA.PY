import os 
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

pdf.set_font('Arial', 'B',18)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 40, 'O aumento de casos de ansiedade e depressão ', align='C', ln=1)
pdf.cell(0, 0, 'durante a pandemia do COVID19', align='C', ln=1)

pdf.set_font('Arial', '', 20)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 227, 'Sara Cristina', align='C', ln=1)
pdf.output("capa.pdf")

os.system("pause")