def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    # yield from gen1() 
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6

# g = gen2(gen1())
g = gen2(gen1)

for n in g:
    print(n)