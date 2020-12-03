
lista=[]
tamanho_lista =int(input('digite tamanho das listas'))
i = 1

while i <= tamanho_lista:
    lista.append(input("Digite um numero para a lista"))
    i+=1

def numero_maior():
    maior = max(lista)
    return maior

print("Esse é o maior numero " + numero_maior())

def numero_menor():
    menor = min(lista)
    return menor

print("Esse é o menor numero " + numero_menor())