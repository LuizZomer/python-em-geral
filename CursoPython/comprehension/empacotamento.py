a, b = 1,2 
a, b = b, a
# print(a,b)

pessoa = {
    'nome' : 'Luiz',
    'sobrenome' : 'Zomer'
}

pessoa2 = {
    'idade': 19,
    'altura': 1.7
}

pessoa_completa = {**pessoa, **pessoa2}

# print(pessoa_completa)

# a, b = pessoa.items() cria uma tupla com as keys e values juntos

# a, b = pessoa.values() Passa para as variaveis apenas os valores

# (a1, a2), b = pessoa.items() #A primeira variavel dentro do parenteses pega a key a segunda pega o valor

# print(a1,a2)
# print(b)

def argumentos_nomeados(*args,**kwargs):
    print(args)
    for chave, valor in kwargs.items():
        print(chave, valor) 

# argumentos_nomeados(1,2,3,nome='Daniel',sobrenome='Obrabo')

argumentos_nomeados(**pessoa_completa)