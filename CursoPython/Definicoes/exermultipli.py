'''Crie Uma função para multiplicar quantos valores o usuario quiser'''




lista = []

def multiplicacao(*args): #Vai transformar em tupla de novo 
    multi = 1
    for numeros in args:
        multi *= numeros #Multiplica todos os valores e joga na variavel
    return multi #Retorna para o escopo externo o valor da variavel multi



while True:
    x = int(input('Escolha um numero: '))
    lista.append(x) #Jogando o numero escolhido na lista
    cont = input('Continuar[S/N]? ').upper()
    if cont in 'N': #caso for 'N' quebra o laço
        break

tupla = tuple(lista) #transformando a lista em tupla

print(multiplicacao(*tupla)) #Vai desenpacotar a tupla e jogar para a função os valores de forma individual / Depois ira printar o valor de multi
