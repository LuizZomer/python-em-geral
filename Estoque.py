from time import sleep

def titulo(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)


def cabecalho():
    print(f'{"nº":<1} |   {"Nome":^5}  |  {"preço":>1}')


def reverso(var):
    print(f'Deseja mostrar o {var} em ordem crescente\n1 - Sim\n2 - Não')
    while True:
        try:
            escolhatxt = input('Selecione a opção: ')
            escolha = int(escolhatxt) 
            if escolha > 2 or escolha < 1:
                print('Essa opção não existe')
            else:
                if escolha == 1:
                    return False
                return True
        except (ValueError, TypeError):
            print('Esse valor não é um numero inteiro')


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
                print('Visualizar por:\n1 - Ordem adicionada\n2 - Nome\n3 - preço')
                filtrotxt = input('Escolha uma opção: ')
                try:
                    filtro = int(filtrotxt)
                except (ValueError,TypeError):
                    print('Opção não é um numero inteiro')
                    sleep(1)
                    continue
                if filtro > 3 or filtro < 1:
                    print('Opção não existente')
                else:
                    match (filtro):
                        case 1:
                            cabecalho()
                            for p in estoque:
                                print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                                cont+=1
                                sleep(0.5)
                        case 2:
                            nome_reverso = reverso('nome')
                            cabecalho()
                            ordenada_nome = sorted(estoque, key=lambda produto: produto['nome'], reverse=nome_reverso )
                            for p in ordenada_nome:
                                print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                                cont+=1
                                sleep(0.5)
                        case 3:
                            preco_reverso = reverso('preço')
                            cabecalho()
                            ordenada_preco = sorted(estoque, key=lambda produto: produto['preco'], reverse=preco_reverso)
                            for p in ordenada_preco:
                                print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                                cont+=1
                                sleep(0.5)
        case 2:
            titulo('Cadastro de produtos')
            produto['nome'] = input('Nome do produto: ')
            while True:
                try:
                    produto['preco'] = float(input('Preço do produto: '))
                    break
                except (ValueError, TypeError):
                    print('Impossivel anexar esse preço ao produto')
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