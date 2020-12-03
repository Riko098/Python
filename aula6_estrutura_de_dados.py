import requests
#INICIANDO ESTRUTURAS DE DADOS VAZIAS
lista = []
tupla= ()
dicionario={}
conjunto=set()

minha_lista = ['erico', 'maria'] #lista
minha_tupla = ('Gui', 'João') #Tupla (tuple) Não é dinamico
#No dicionario os dados possuem chave e valor
meu_dicionario = {'nome': 'Guilherme', 'idade': 27} #Dicionario (Dict)
#No conjunto nao posso colocar itens repetidos nem é ordenado nao possui indice
meu_conjunto={'Gui', 'Joao'}#Conjunto(set)

if 'Gui' in minha_tupla:#Codigo para procurar um item em uma coleção MENOS EM DICIONARIO
    print('Gui esta na coleção')


print(meu_dicionario['nome'])#Fazendo busca no dicionario é feita pelo indice nesse caso o nome
#Codigo para buscar um item no DICIONARIO
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme esta no dicionario')

#OBSERVAÇÃO EM QUESTAO DE BUSCA CONJUNTO É A MELHOR COLEÇÃO POIS É MAIS RAPIDA  PQ USA TABELA HASH