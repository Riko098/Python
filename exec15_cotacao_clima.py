
import requests
import json
cidade = input('escreva sua cidade')
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=0266d05972b3dfc45d5925fc4eca2cca')
print(requisicao.text)