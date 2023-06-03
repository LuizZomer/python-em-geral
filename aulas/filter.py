def filtrar_preco(p):
    return p['preço'] > 15

produtos = [
    {'nome':'p1','preço':20},
    {'nome':'p3','preço':10},
    {'nome':'p4','preço':30},
    {'nome':'p2','preço':5},
    {'nome':'p5','preço':50}
]

# novos_produtos = [
#     p for p in produtos if p['preço'] > 10
# ]

novos_produtos = list(filter(
    # lambda p: p['preço'] > 10,
    filtrar_preco,
    produtos)
)  

print(novos_produtos)