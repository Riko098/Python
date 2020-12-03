frase='oi, tudo bem?'

print(frase.lower())#Deixa toda string toda em minusculo
print(frase.upper())#Deixa toda a string e maisculo
print(len(frase))#O len serva para contar o que tem dentro de qualquer tipo de coleção
print(frase[0])#Imprimi o primeiro caractere da string
frase_separada = frase.split(',')#Separa a string onde tiver ',' e a transforme em uma lista
print(frase_separada)

lista=['moto','carro', 'avião', 'avião']
lista.append('nave')# o .append serve para adicionar um item a lista
lista.remove('moto')# o .remove serve para remover um item da lista
lista.insert(0, 'Creosvaldo')#O .insert serve para adicionar im item em determinada posição
lista[1] = 'Erico' #Deste modo coloco um item na lista no lugar do outro
contador_aviao=lista.count('avião')

print(contador_aviao)
print(lista)
print(lista.pop())#Retira o primeiro item de qualquer coleção
#print(lista[0:10:2])#para imprimir o ultimo item de uma lista basta usar o indice "-1"

