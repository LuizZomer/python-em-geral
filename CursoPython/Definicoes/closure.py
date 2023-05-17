def nome(saudacao):
    def sauda(nome):
        return f'{saudacao}, {nome}!'
    return sauda

saudacao1 = nome('Bom dia') 

print(saudacao1('Luiz'))