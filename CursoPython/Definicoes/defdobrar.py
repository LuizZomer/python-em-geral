def dobrar(lst):
    for i,v in enumerate(lst):
        lst[i] = v * 2
    
    print(lst)


lista = [1,2,3,4,5]
dobrar(lista)