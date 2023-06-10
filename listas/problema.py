def clientes(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = clientes('Luiz')
clientes('Maria',cliente1)

print(cliente1)