salas = [
    ['Luiz','Willian','André',],

    ['Maria', 'Oseias', 'Luis', (12,43,56)],

    ['Jean','Cauã','Henrique',]
]

print(salas[1][3][1])

for sala in salas:
    print(sala)
    for alunos in sala:
        print(alunos)