from time import sleep

def titulo(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)

produto = {}

estoque = []

while True:
    cont = 0
    titulo('estoque')
    print('1 - visualizar estoque\n2 - cadastrar produtos\n3 - apagar produtos\n4 = Sair do programa')
    opcaotxt = input('Escolha uma opção: ')
    try:
        opcao = int(opcaotxt)
    except ValueError:
        print('Valor invalido')
        sleep(1)
        continue    
    match opcao:
        case 1:
            titulo('Visualização do estoque')
            if len(estoque) == 0:
                print('O estoque está vazio')
                sleep(1)
            else:
                print(f'{"nº":<1} |   {"Nome":^5}  |  {"preço":>1}')
                for p in estoque:
                    print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                    cont+=1
                    sleep(1)
        case 2:
            titulo('Cadastro de produtos')
            produto['nome'] = input('Nome do produto: ')
            produto['preco'] = input('Preço do produto: ')
            print(f'O produto {produto["nome"]} foi cadastrado com sucesso.')
            estoque.append(produto.copy())
            produto.clear()
            sleep(1)
        case 3:
            deletartxt = input('Escolha o numero do produto para excluir: ')
            try:
                deletar = int(deletartxt)
            except ValueError:
                print('Valor incorreto')
            if deletar > len(estoque)-1:
                print('Numero inxistente')
            else:
                print(f'O produtos {estoque[deletar]["nome"]} foi apagado com sucesso')
                estoque.pop(deletar)
                sleep(1)
        case 4:
            print('Saindo do programa...')
            break
        case _:
            print('Opção invalida')
            sleep(1)