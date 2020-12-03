import requests
import json

def requisicao(titulo):
    try:
        requisicaoapi = requests.get('http://www.omdbapi.com/?t='+titulo+'&type=movie&apikey=69e0e2e2')
        dicionario = json.loads(requisicaoapi.text)
        return dicionario
    except:
        print('erro na requisição')
        return None

#print(requisicaoapi.text)
def printar_detalhes(filme):
    print('Título:',filme['Title'])
    print('Lançamento:',filme['Year'])
    print('Principais Atores:',filme['Actors'])
    print('Genero:', filme['Genre'])
    print('Diretor:', filme['Director'])
    print('Nota:', filme['imdbRating'])
    print('Poster do Filme:', filme['Poster'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme ['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)
