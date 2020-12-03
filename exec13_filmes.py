import requests
import json


def lista_filmes(titulo):
    lista=[]
    for i in range(1, 101):
        try:
            print('Pesquisando em pagina', i)
            req = requests.get('http://www.omdbapi.com/?s='+titulo+'&type=movie&page='+str(i)+'&apikey=69e0e2e2')
            resposta=json.loads(req.text)
            if resposta['Response']=='True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano=filme['Year']
                    string = tit+ ' ('+ ano + ')'
                    lista.append(string)

            else:
                print('Fim das paginas')
                break
        except:
            print('conexao falhou')
    return lista

#print(listafilmes('matrix'))
sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar')
    if op == 'SAIR':
        sair='True'
        print('Saindo...')
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)

'''
    req = requests.get('http://www.omdbapi.com/?s=titanic&page=1&apikey=69e0e2e2')
    dicionario=json.loads(req.text)
    print(dicionario['Search'][0]['Title'])
    
'''