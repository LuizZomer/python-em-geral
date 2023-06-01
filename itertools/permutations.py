# permutations,combinations e product

from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()

pessoas = [
    'joão','Joana','Luiz','Leticia'
]

camisetas = [
    ['preta','branca'],
    ['p','m','g'],
    ['maculino','feminino','unisex'],
    ['algodão','poliéster']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))