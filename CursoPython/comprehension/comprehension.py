# Basico

# lista = [numero for numero in range(10)] #A esqueda a variavel que será adicionada na lista, o resto é a logica

# lista = [numero*2 for numero in range(10)] #Agora com uma operação 

# print(lista)


# l = [numero for numero in range(11)]

# print(l)

# Um pouco mais avançado

produtos = [
    {'nome':'p1','preço':20},
    {'nome':'p2','preço':10},
    {'nome':'p3','preço':30}
]

# novos_produtos = [produto['nome'] for produto in produtos]
novos_produtos = [{**produto,'preço':produto['preço'] * 1.05} if produto['preço'] > 20 else {**produto} for produto in produtos] #Alterando o preço do dict antigo e criando um novo dict com os valores
 

print(*novos_produtos, sep='\n')