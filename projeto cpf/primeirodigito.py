cpf_origin = '988.360.917-50'.split('.')

cpf_sem_ponto = ''.join(cpf_origin)

cpf_lista = cpf_sem_ponto.split('-')

cpf_9dig = cpf_lista[0]

lista_str = []

for numero in cpf_9dig:
    lista_str.append(numero)

print(lista_str)

cont = 10
soma = 0

lista_int = []

for digito in lista_str:
    digito_int = int(digito)
    lista_str.append(digito_int)

for digito in lista_str:
    mult = 0
    mult = digito*cont
    soma+=mult
    cont-=1

print(lista_str)
print(soma)


