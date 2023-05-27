def generator(n=0, maximum=10):
    # yield 1 #pause
    # # return 'acabou'
    # print('Continuando...')
    # yield 2 #pause
    # print('De novo!')
    # yield 3
    # print('Ultimo')
    # return 'Fim'
    while True:
        yield n
        n +=1

        if n > maximum:
            return 

gen = generator(n = 20, maximum=1000)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
