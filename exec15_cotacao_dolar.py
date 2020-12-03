import requests
import json
import datetime#Biblioteca para consultar o horário

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD')
cotacao = json.loads(requisicao.text)
print('Horário', datetime.datetime.now())
print('O dolár foi cotado no maior valor hoje de:',cotacao['USD']['high'])
print('O dolár foi cotado no menor  valor hoje de:',cotacao['USD']['low'])


''' USD: {
{'USD': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Comercial', 'high': '5.2177', 'low': '5.2177', 'varBid': '0.0003', 'pctChange': '0', 'bid': '5.2175', 'ask': '5.218', 'timestamp': '1606948556', 'create_date': '2020-12-02 21:00:03'}}

        code: "USD",
        codein: "BRL",
        name: "Dólar Comercial",
        high: "3,8906",
        low: "3,8596",
        varBid: "-0,0138",
        pctChange: "-0,36",
        bid: "3,8660",
        ask: "3,8680",
        timestamp: "1555360069",
        create_date: "2019-04-15 17:27:50" }'''