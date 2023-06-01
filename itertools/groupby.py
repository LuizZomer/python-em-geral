from itertools import groupby

def ordena(aluno):
    return aluno['nota']

alunos = [
    {'nome':'Luiz','nota':'A'},
    {'nome':'Leticia','nota':'B'},
    {'nome':'Fabricio','nota':'B'},
    {'nome':'Joana','nota':'A'},
    {'nome':'André','nota':'C'},
    {'nome':'Rose','nota':'C'},
    {'nome':'Anderson','nota':'D'},
]

ordenado = sorted(alunos, key=ordena)

# notas = ['A','A','A','A','A','B','C','A']

# grupos = groupby(sorted(notas))
grupos = groupby(ordenado,key=ordena)

for chave,grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)