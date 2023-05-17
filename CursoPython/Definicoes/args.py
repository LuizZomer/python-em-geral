def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total



numeros = 1,2,3,4,5

print(soma(*numeros))
print(sum((1,2,3,4,5)))
