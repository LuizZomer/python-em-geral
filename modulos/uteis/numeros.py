def fatorial(num, show=True):
    f = 1
    if show:
        for n in range(num,0,-1):
            f *=n
            if n > 1:
                print(n, end=' x ')
            else:
                print('1 = ', end='')
        print(f)


def leiaInt(num):
    if num.isnumeric():
        return 'É um numero inteiro'
    else:
        return 'Não é um numero inteiro'

