import os
lista = []


while True:
    erro = None
    escolha = input('[L]istar  [A]pagar  [i]nserir: ').upper()
    match escolha:
        case 'L':
            
            if len(lista) == 0:
                print('Nada para listar')

            for item in enumerate(lista):
                print(item)
        case 'A':
            apagar_str = input('Qual indice deseja apagar: ')

            try:
                apagar_int = int(apagar_str)
            except ValueError:
                print('Não é um numero')
                erro = True


            if erro is None:
                if apagar_int > len(lista)-1:
                    print('Indice inesistente!')
                else:
                    lista.pop(apagar_int)
        case 'I':
            inserir = input('Insira um item: ')
            lista.append(inserir)
        case _:
            print('Escolha uma opção existente')
            


