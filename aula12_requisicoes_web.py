#GET em um requisição solicita
#POST em uma requisiçao envia dados


import requests
cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'www.google.com',
             'CDN-LOOP': 'Amazon',
             'VERSION': 'ERICO'}
meus_cookies = {'Ultima-visita': '10-10-1350'}
dados ={'username': 'ericopp98',
        'password': 'erico123'}

texto = None
try:
    requisicao = requests.post('https://putsreq.com/aV6Ej1zVuEFZsnkAcvIJ',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print('requisição falhou', e)

print(texto)