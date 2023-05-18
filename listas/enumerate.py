lista = ['django','el rabib', 'é o vasco', 'werner']

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

for i, n in enumerate(lista):
    print(i,n)