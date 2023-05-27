import sys

iterable = ['eu','tenho','__iter__']
iterator = iterable.__iter__()

lista = [n for n in range(100000)]
generator = (n for n in range(100000))

print(sys.getsizeof(lista))

print(sys.getsizeof(generator))

for n in generator:
    print(n)