produto = {
    'nome':'caneta',
    'preço':2.5,
    'categoria': 'escritorio'
}

dc ={
    chave:valor.upper() if isinstance(valor,str ) #Se for colocar mais de 2 tipos tem q ser em uma tupla. Ex:(int,float)
    else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

print(dc)

#Set comprehension

s1 = set(i*2 if i > 5 else i for i in range(11) if i %2 ==0)

print(s1)