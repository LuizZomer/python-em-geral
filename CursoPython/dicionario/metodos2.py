nome = {'nome':'Luiz', 'sobrenome':'Zomer', 'idade':19}

print(nome.get('nome'))

# nome1 = nome.pop('nome')

# print(nome1)

ultima_chave = nome.popitem()

print(ultima_chave)

# nome.update({
#     'nome':'Jefferson',
#     'altura': 1.7
# })

nome.update(nome='Jeferson',altura=1.7)

print(nome)