from functools import partial


def aumentar_porcentagem(valor,porcentagem):
    return round(valor * porcentagem, 2)


dezporcento = partial(aumentar_porcentagem, porcentagem=1.1)

produtos = [
    {'nome':'p1','preço':20},
    {'nome':'p3','preço':10},
    {'nome':'p4','preço':30},
    {'nome':'p2','preço':5},
    {'nome':'p5','preço':50}
]

# novos_produtos = [
#     {**p,'preço':dezporcento(p['preço'])} for p in produtos
# ]

def muda_preco(produto):
    return {**produto,'preço':dezporcento(produto['preço'])}


novos_produtos = list(map(muda_preco,produtos))

print(novos_produtos)

print(list(map(lambda x: x *3,[1,2,3,4])))