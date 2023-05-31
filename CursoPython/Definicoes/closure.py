def nome(saudacao):
    def sauda(nome):
        return f'{saudacao}, {nome}!'
    return sauda

saudacao1 = nome('Bom dia') 

print(saudacao1('Luiz'))


def concatenar(string):
    valor_inicial = string
    def interna(valor_final):
        nonlocal valor_inicial
        valor_inicial += valor_final
        return valor_inicial
    return interna


c = concatenar('a')
print(c('b'))