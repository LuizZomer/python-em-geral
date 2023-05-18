nome = input('Escreva seu nome: ')
idade = input('Sua idade: ')


if nome and idade:
    print(f'Seu nome é {nome}.\nSeu nome invertido é {nome[::-1]}\n')
    if ' ' in nome:
        print('Tem espaço no seu nome')
    else:
        print('Não tem espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}\nA ultima é {nome[len(nome)-1]}')
else:
    print('Deixou campos vazios')
