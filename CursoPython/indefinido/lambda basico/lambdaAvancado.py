def executa(funcao,*args):
    return funcao(*args)

# def soma(x,y):
#     return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


print(executa(lambda x,y: x + y,2,3)) #Isso é igual a função soma(x,y)
# print(executa(lambda x,y,z: x + y + z, 2,2,6))

duplica = executa(
    lambda m: lambda n: n*m,3 #método não recomendado pela PEP 8, é mais recomendado usar a função cria_multiplicador
)

print(duplica(2))

print(
    executa(
    lambda *args: sum(args),1,2,3,4,5  #Soma todos os parametro q ela for receber
    )
)