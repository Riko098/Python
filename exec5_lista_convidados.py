
'''EXERCICIO: Faça um programa que leia a quantidade de pessoas que serão convidados para uma festa
Ápos isso o programa irá perguntar o nome de todas as pessoas e colocar em uma lista de convidados
Apos isso irá imprimir todos os nome da lista
'''

quantidade_pessoas=int(input('Digite a quantidade de convidados:'))
lista_convidados=[]
i = 1

while i <= quantidade_pessoas:
    lista_convidados.append(input('Digite o nome do Convidado#' + str(i) +':'))
    i +=1
print('\nLista de Convidados')
for convidados in lista_convidados:
     print(convidados)
