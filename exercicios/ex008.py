import copy

produtos = [
    {'nome':'produto1','preco':10.00},
    {'nome':'produto5','preco':22.32},
    {'nome':'produto3','preco':10.11},
    {'nome':'produto4','preco':105.87},
    {'nome':'produto2','preco':69.90},
]

novos_produtos = [{**produto,'preco': round(produto['preco'] * 1.1,2)} for produto in copy.deepcopy(produtos)]

print('Produtos com 10% mais mais caro',novos_produtos)

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda item: item['nome'], reverse= True)

print('Ordenado por nome decrecente',produtos_ordenados_por_nome)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda item: item['preco'] )

print('Ordenado por preço',produtos_ordenados_por_preco)