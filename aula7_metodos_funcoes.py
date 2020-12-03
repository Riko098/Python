#FUNÇÕES
print("Olá Mundo")
len("Olá Mundo")

#Criando uma funçãoa de soma
def soma(numero1, numero2):
    resposta=numero1+numero2
    return resposta

retorno=soma(10, 2)
print(retorno)

def imprime_oi():
    print('OI')

imprime_oi()
imprime_oi()
imprime_oi()

'''def pergunta():
    nome=input('Digite seu nome')
    print(nome)
    return nome

pergunta()'''

def tem_sete_letras(argumento):
    if len(argumento)==7:
        return True
    else:
        return False

if (tem_sete_letras('1234567')):
    print('Tem sete letras')