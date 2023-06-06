from sys import exit

def titulo(msg): #Pega a mensagem passada e transforma em um titulo
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)


def verificador(num,tipo):
    var_teste,veri = eh_valor(num,tipo) #Função para ver se é mesmo um numero
    if veri:
        while var_teste:
            num = input('ERRO!Digite um valor valido: ') #Vai entrar em looping até o usuario digitar um valor valido
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

produtos = {'Arroz':{'valor':4.70,'quantidade':5},'Feijão':{'valor':4.70,'quantidade':5},'Pedra':{'valor':4.70,'quantidade':5},}

while True: #Loop infinito
    titulo('Estoque')
    print('1 - Vizializar estoque\n2 - Editar estoque\n3 - Sair do programa') #Menu
    escolhatxt = input('Escolha a opção: ')
    escolha = verificador(escolhatxt,int)
    match escolha:
        case 1:
            print('1 - visualizar produtos\n2 - Relatório do estoque')

        case 2: #Edição do estoque
            titulo('Edição do estoque')
            print('1 - Adicionar produto\n2 - deletar produto\n3 - Atualizar produto\n4 - Voltar')

            escolha1txt = input('Escolha uma opção: ') #Escolha do menú, mas ainda em string
            escolha1 = verificador(escolha1txt,int)

            match escolha1:
                case 1: #Adicionando produto
                    nome = input('Nome do produto: ').capitalize()
                    valortxt = input('O preço da unidade do produto: ') #valor do produto em string
                    valor = verificador(valortxt,float) #Após entrar no verificador, ele retorna o tipo certo
                    quantidadetxt = input('A quantidade do produto: ') #quantidade do produto em string
                    quantidade = verificador(quantidadetxt,int) #Após entrar no verificador, ele retorna o tipo certo
                    produtos[nome] = {'valor': valor, 'quantidade': quantidade}

                case 2: #Deletando um produto
                    deletar = input('Nome do produto que deseja deletar(por nome): ').capitalize()
                    if deletar in produtos:
                        print(f'O produto {produtos[deletar]} foi apagado com sucesso')
                        del produtos[deletar]
                    else:
                        print('Produto inexistente')

                case 3: #Editar estoque
                    editar = input('Digite o nome do produto para a edição: ').capitalize()

                    if editar in produtos: #Verificar se há o nome dentro do dicionario
                        print('1 - valor\n2 - quantidade')
                        escolhatxt = input('Escolha a opção: ')
                        escolha = verificador(escolhatxt,int)

                        if escolha == 1: # valor
                            valor1txt = input(f'Qual o valor você deseja atribuir ao produto {editar}: ')
                            valor1 = verificador(valor1txt,float)
                            produtos[editar]['valor'] = valor1
                            print(f'Atualizado com sucesso, agora {editar} vale {produtos[editar]["valor"]} reais')
                            
                        elif escolha == 2: #Quantidade
                            quantidade1txt = input(f'Qual a quantidade você deseja atribuir ao produto {editar}: ')
                            quantidade = verificador(quantidade1txt,int)
                            produtos[editar]['quantidade'] = quantidade
                            print(f'Atualizado com sucesso, agora {editar} tem {produtos[editar]["valor"]} produtos no estoque')
                            print(produtos)
                        else: # Nenhuma opção
                            print('Opção invalida!')

                    else:
                        print('Produto inexistente')
                    
                case 4: #Voltar
                    continue

                case _: #Nenhuma opção selecionada
                    print('Opção inexistente')



            
            
            
            
            
                





