# pessoa = {
#     'nome': 'Zomito',
#     'nick': 'jooj14',
#     'altura': 1.7,
#     'idade' : 19,
#     'endereco' : [{'rua': 'Chapecó', 'bairro':'Jardim Elizabeth'},{'cidade':'Cocal do sul', 'estado': 'Santa Catarina'}]
# }

# pessoa = dict(nome = 'Zomito', nick = 'Jooj14')

# print(pessoa)

# print(pessoa['nick'])

pessoa = {}

pessoa['sobrenome'] = 'Obrabo'

chave = 'nome'

pessoa[chave] = 'Luizada'


print(pessoa)

del pessoa['sobrenome']

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Ja foi de vapo')
else:
    print(pessoa['sobrenome'])
