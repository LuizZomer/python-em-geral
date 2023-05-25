# l = [1,2,3,4,5]

l = [
    {'nome':'Luiz','sobrenome':'Zomer'},
    {'nome':'Maria','sobrenome':'Silva'},
    {'nome':'Arthur','sobrenome':'Silveira'},
    {'nome':'Eduardo','sobrenome':'Garcia'}
]

# def ordena(item): Ordena o dicionario pela chave nome
#     return item['nome']

# def ordena(item): Ordena o dicionario pelo sobrenome
#     return item['sobrenome']


# l.sort(key=lambda item: item['nome']) Realmente modifica a lista
l1 = sorted(l, key=lambda item: item['nome']) #Faz uma copia rasa da lista para a variavel

for pessoa in l1:
    print(pessoa)



