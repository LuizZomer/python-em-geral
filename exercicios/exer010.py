# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1),len(lista2))
#     return[
#         (lista1[i],lista2[i]) for i in range(intervalo_maximo)
#     ]

from itertools import zip_longest

l1 = ['Salvador','Ubatuba','Belo Horizonte']
l2 = ['BA','SP','MG','RJ', 'SC']
print(list(zip(l1,l2))) # Itera sobre a menor lista
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE'))) # Itera sobre a maior lista