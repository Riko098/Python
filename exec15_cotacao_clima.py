
import requests
import json
import datetime

cidade = input('escreva sua cidade')
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=0266d05972b3dfc45d5925fc4eca2cca')
informacoes_tempo=json.loads(requisicao.text)

'''trad_condicao = (informacoes_tempo['weather'][0]['main'])
print(trad_condicao)'''
print('O clima de '+cidade+' é:',informacoes_tempo['weather'][0]['main'])
print('Temperatura é',float(informacoes_tempo['main']['temp'])-273.15)

print('Horário', datetime.datetime.now())

'''if trad_condicao== 'Rain':
    print('Tempo chuvoso')'''

