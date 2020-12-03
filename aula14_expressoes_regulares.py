#email@dominio.com.br
import re
import requests

url = requests.get('https://zecoxinha.com.br/contato/')
stringdeteste = 'ericopeixoto@gmail.com'

padrao=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', url.text)

if padrao:
    print(padrao)
else:
    print('padrao na encontrado')

