while True:
    print('Calculadora')
    num_str = input('Escolha um numero: ')
    num_str1 = input('Escolha outro numero: ')

    numero_msm = None
    operador_msm = None
    erro = None

    try:
        num1 = float(num_str)
        num2 = float(num_str1) 
        numero_msm = True
    except:
        print('Não é um numero')
        erro = True
    
    if numero_msm is True:
        operador = input('Escolha o operador[+-*/]: ')
    
    if len(operador) != 1 or operador not in '+-*/'  :
        print('Digite apenas 1 operador ou operador invalido')
        erro= True
    
    if erro is None:
        print(f'{num1} {operador} {num2} é igual a:')
        match operador:
            case '+':
                print (num1 + num2)
            case '-':
                print(num1 - num2)
            case '*':
                print(num1 * num2)
            case '/':
                try:
                    print(num1 / num2)
                except ZeroDivisionError:
                    print('Não dá de dividir por zer0')

            

        

    
        