nomes = ['Erico', 'Mariana', 'João', 'Guilherme']
for nome in nomes:
    print(nome)

lista_de_numero=range(0, 100, 2)#A função range cria uma lista com o tamanho especifico neste caso(0,100)e o numero(2) é o passo que vai pulando entre eles
for item in lista_de_numero:
    print(item)

palavra = 'bola'
for letras in palavra:
    print(letras)

#Usando o while

i = 0
while i < 10:
    print('I ainda menor que 10:', i)
    i = i+1
