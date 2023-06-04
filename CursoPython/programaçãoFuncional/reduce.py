from functools import reduce

def funcao_total(total,produto):
    return total + produto['preço']


produtos = [
    {'nome':'p1','preço':20},
    {'nome':'p3','preço':10},
    {'nome':'p4','preço':30},
    {'nome':'p2','preço':5},
    {'nome':'p5','preço':50}
]

total = reduce(
    # lambda acumulador, produto: acumulador + produto['preço'],
    funcao_total,
    produtos,
    0
)

print(total)