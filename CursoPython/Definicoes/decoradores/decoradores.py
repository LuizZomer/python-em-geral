def is_int(func):
    def confirmar(*args):
        for arg in args:
            if not isinstance(arg, (int,float)):
                raise TypeError('Valor digitado não é um int ou float')
        return func(*args)
    return confirmar


@is_int
def soma(x,y):
    return x + y


print(soma(4,14))