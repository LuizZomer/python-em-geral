import pprint 

#mapeamento o if vem antes do for, para o filtro o if vem depois

lista = [n for n in range(31) if n > 5]

# print(lista)

nova = [numero * 2 if numero % 2 == 0 else numero for numero in lista if numero > 20]

nova_ordenada = sorted(nova)

print(nova_ordenada)
