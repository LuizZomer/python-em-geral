from time import sleep

def titulo(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)

produto = {}

estoque = []

while True:
    titulo('estoque')
    print('1 - visualizar estoque\n2 - cadastrar produtos\n3 - fechar programa')
    opcaotxt = input('Escolha uma opção: ')
    try:
        opcao = int(opcaotxt)
    except ValueError:
        print('Valor invalido')
        continue
    match opcao:
        case 1:
            titulo('Visualização do estoque')
            if len(estoque) == 0:
                print('O estoque está vazio')
            else:
                print(f'{"Nome":<10}  |  {"preço":>1}')
                for p in estoque:
                    print(f'{p["nome"]:<10} {p["preco"]:>10}')
        case 2:
            titulo('Cadastro de produtos')
            produto['nome'] = input('Nome do produto: ')
            produto['preco'] = input('Preço do produto: ')
            print(f'O produto {produto["nome"]} foi cadastrado com sucesso.')
            estoque.append(produto.copy())
            produto.clear()
        case 3:
            print('Saindo do programa...')
            break
        case _:
            print('Opção invalida')