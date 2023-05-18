lista = [1, 1.5, 'Zomito', True]
lista[2] = 'Zomagico'
del lista[3]

print(lista)

lista.append('esqueça') #adiciona um item no final

print(lista)

lista.pop() #Remove um item da lista, quando está vazio ele tira o ultimo

lista.append(23)

ultimo_valor = lista.pop()

primeiro_valor = lista.pop(0)

print('Primeiro valor da lista:',primeiro_valor)
print('Ultimo valor da lista:',ultimo_valor)
print(lista)

del lista[-1] #apaga um item ou a lista
lista.clear() #Limpa a lista

lista.insert(0, 'Teste') #primeiro valor é a posição, o segundo é oque eu quero adicionar

lista.insert(0, 'toma')

print(lista)

lista_a = [0,1,2,3]
lista_b = [4,5,6,7]
lista_c = lista_a + lista_b

print('Lista unida', lista_c)

lista_a.extend(lista_b)
print('Essa é a lista A',lista_a)

for item in lista_a:
    print(item)