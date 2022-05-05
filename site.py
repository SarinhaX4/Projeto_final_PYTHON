import os, requests
from bs4 import BeautifulSoup

urld1 = requests.get('https://covid.saude.gov.br/')
d1 = urld1.content

sited1 = BeautifulSoup(d1, 'html.parser')
respd1 = sited1.find('_ngcontent-nav-c6')


if respd1:
    print(respd1)
else:
    print("O elemento não foi encontrado no HTML!")

os.system("pause")