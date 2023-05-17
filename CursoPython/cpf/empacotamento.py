lista = ['luiz','dream','rabib',1,2,3,'terne']

a,b,*_,ap,u = lista
print(a,ap)

print(*lista)
print(*lista, sep='\n')