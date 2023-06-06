def titulo(msg): #Pega a mensagem passada e transforma em um titulo
    print('='*20)
    print(f'{msg:^20}')
    print('='*20)


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
    print('1 - Adicionar produto\n2 - deletar produto\n3 - visualizar produtos\n4 - Atualizar estoque\n5 - relatorio do estoque\n5 - Sair do programa') #Menú
    escolhatxt = input('Escolha uma opção: ') #Escolha do menú, mas ainda em string
    try:
        escolha = int(escolhatxt) #O sistema vai tentar transformar a resposta do usuario em inteiro, caso consiga o sistema seguirá normalmente
    except: 
        print('Valor incorreto') #Caso ele não consiga irá aparecer essa mensagem como se você um erro
        continue #Fará o looping começar de novo

    match escolha:
        case 1: #Adicionando produto
            nome = input('Nome do produto: ').capitalize()
            valortxt = input('O preço da unidade do produto: ') #valor do produto em string
            valor = verificador(valortxt,float) #Após entrar no verificador, ele retorna o tipo certo
            quantidadetxt = input('A quantidade do produto: ') #quantidade do produto em string
            quantidade = verificador(quantidadetxt,int) #Após entrar no verificador, ele retorna o tipo certo
            produtos[nome] = {'valor': valor, 'quantidade': quantidade}
        case 2:
            deletar = input('Nome do produto que deseja deletar(por nome): ').capitalize()
            print(deletar)
            if deletar in produtos:
                print(f'O produto {produtos[deletar]} foi apagado com sucesso')
                del produtos[deletar]
            else:
                print('Produto inexistente')
            
            
            
            
            
                





