lista = ['a',1,2.2,True,[0,1,2],(1,2),{0,1},{'nome':'Luiz'}]

for item in lista:
    if isinstance(item,set):
        print('set')
        item.add(5)
        print(item,isinstance(item, set))
    elif isinstance(item,str):
        print('string')
        print(item.upper() ,isinstance(item, str))
    elif isinstance(item,(int,float)):
        print('numero')
        print(item, item *2)
    else:
        print('outro')
        print(item)