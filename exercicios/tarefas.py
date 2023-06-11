tarefas = []
tarefas_excluidas = []

while True:
    print('listar,tirar,refazer')
    escolha = input('Escolha: ')
    match escolha:
        case 'listar':
            for num,item in enumerate(tarefas):
                    print(f'{num} - {item}')
        case 'tirar':
            excluido = tarefas.pop()
            tarefas_excluidas.append(excluido)
        case 'refazer':
                voltar = tarefas_excluidas.pop()
                tarefas.append(voltar)
        case _:
              tarefas.append(escolha)
    for num,item in enumerate(tarefas):
        print(f'{num} - {item}')
    