import json

# pessoa = {
#     'nome': 'Zomito',
#     'nick': 'jooj14',
#     'altura': 1.7,
#     'idade' : 19,
#     'endereco' : [{'rua': 'Chapecó', 'bairro':'Jardim Elizabeth'},{'cidade':'Cocal do sul', 'estado': 'Santa Catarina'}]
# }

# with open('teste.json','w',encoding='utf8') as arquivo:
#     json.dump(pessoa,arquivo,indent=2)

with open('teste.json','r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])



