from sys import exit

def titulo(msg): #Pega a mensagem passada e transforma em um titulo
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)


def erro(con):
    print(f'{con} inexistente')


def verificador(num,tipo):
    var_teste,veri = eh_valor(num,tipo) #Função para ver se é mesmo um numero
    if veri:
        while var_teste:
            num = input('ERRO!Digite um valor valido: ').replace(',','.') #Vai entrar em looping até o usuario digitar um valor valido
            var_teste,veri = eh_valor(num,tipo) #Chama a função de verificação 
        return tipo(num)
    else:
        return tipo(num)


def eh_valor(num,tipo): #Olhando se ele é um numero
    try:
        tipo(num) #Tentando converter a string no tipo que eu mandar
        
        return False, False #O primeiro valor é para o var_teste, o segundo é para o veri
    except ValueError:
        return True, True #Igual a cima
    


#Código principal

produtos = {}

while True: #Loop infinito
    titulo('Estoque')
    print('1 - Vizualizar estoque\n2 - Editar estoque\n3 - Sair do programa') #Menu
    escolha3txt = input('Escolha a opção: ')
    escolha3 = verificador(escolha3txt,int)
    match escolha3:
        case 1: #Visualização do estoque
            if len(produtos) == 0:
                print('O estoque está Vazio')
            else:
                titulo('Vizualização do estoque')
                print('1 - visualizar produtos\n2 - Relatório do estoque')
                escolhatxt = input('Escolha a opção: ')
                escolha = verificador(escolhatxt,int)

                match escolha: #Visualizar os produtos
                    case 1:
                        for p in produtos.keys():
                            print(p)

                    case 2: #Relatório do estoque
                        while True:
                            print('1 - Valor total do estoque\n2 - Quantidade total do estoque\n3 - Produtos detalhados\n4 - Sair')
                            escolhatxt = input('Escolha uma opção: ')
                            escolha = verificador(escolhatxt,int)

                            match escolha:
                                case 1: #Valor total do estoque
                                    valor_inicial = 0
                                    quantidade_total = 0
                                    for p in produtos.values():
                                        valor_inicial += p['valor']
                                        quantidade_total += p['quantidade']
                                    valor_total = valor_inicial * quantidade_total
                                    print(f'O valor total do estoque é {valor_total:.2f} reais')

                                case 2: #Quantidade total do estoque
                                    quantidade_total = 0
                                    for p in produtos.values():
                                        quantidade_total += p['quantidade']
                                    print(f'A quantidade total do estoque é {quantidade_total} unidades.')
                                
                                case 3: # Informações dos produtos
                                    for k,v in produtos.items():
                                        print(f'O produto {k} tem {v["quantidade"]} unidades e custam {v["valor"]} cada.')

                                case 4: #Voltar
                                    break

                                case _: #Nenhuma opção selecionada 
                                    erro('Opção')
                            

                    case _: #Nenhuma opção 
                        erro('Opção')


        case 2: #Edição do estoque
            titulo('Edição do estoque')
            print('1 - Adicionar produto\n2 - deletar produto\n3 - Atualizar produto\n4 - Voltar')

            escolha1txt = input('Escolha uma opção: ') #Escolha do menú, mas ainda em string
            escolha1 = verificador(escolha1txt,int)

            match escolha1:
                case 1: #Adicionando produto
                    nome = input('Nome do produto: ').capitalize()
                    valortxt = input('O preço da unidade do produto: ').replace(',','.') #valor do produto em string
                    valor = verificador(valortxt,float) #Após entrar no verificador, ele retorna o tipo certo
                    quantidadetxt = input('A quantidade do produto: ') #quantidade do produto em string
                    quantidade = verificador(quantidadetxt,int) #Após entrar no verificador, ele retorna o tipo certo
                    produtos[nome] = {'valor': valor, 'quantidade': quantidade}

                case 2: #Deletando um produto
                    deletar = input('Nome do produto que deseja deletar(por nome): ').capitalize()
                    if deletar in produtos: #Caso tenha o item no dicionario
                        print(f'O produto {deletar} foi apagado com sucesso')
                        del produtos[deletar]
                    else: #Caso não tenha
                        erro('Produto')

                case 3: #Editar estoque
                    editar = input('Digite o nome do produto para a edição: ').capitalize()

                    if editar in produtos: #Verificar se há o nome dentro do dicionario
                        print('1 - valor\n2 - quantidade')
                        escolha3txt = input('Escolha a opção: ')
                        escolha3 = verificador(escolha3txt,int)

                        if escolha3 == 1: # valor
                            valor1txt = input(f'Qual o valor você deseja atribuir ao produto {editar}: ')
                            valor1 = verificador(valor1txt,float)
                            produtos[editar]['valor'] = valor1
                            print(f'Atualizado com sucesso, agora {editar} vale {produtos[editar]["valor"]} reais')
                            
                        elif escolha3 == 2: #Quantidade
                            quantidade1txt = input(f'Qual a quantidade você deseja atribuir ao produto {editar}: ')
                            quantidade = verificador(quantidade1txt,int)
                            produtos[editar]['quantidade'] = quantidade
                            print(f'Atualizado com sucesso, agora {editar} tem {produtos[editar]["valor"]} produtos no estoque')
                            print(produtos)
                        else: # Nenhuma opção
                            erro('Opção')

                    else:
                        erro('Produto')
                    
                case 4: #Voltar
                    continue

                case _: #Nenhuma opção selecionada
                    erro('Opção')
        
        case 3:
            exit()
        
        case _:
            erro('Opção')



            
            
            
            
            
                





