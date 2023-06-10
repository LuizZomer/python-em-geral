caminho = 'banco.txt'

# arquivo = open(caminho,'w')

# arquivo.close()

# with open(caminho,'w') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2')

with open(caminho,'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    # arquivo.seek(0,0)
    # print(arquivo.read())
    arquivo.writelines(
        ('linha 3\n','linha 4')
    )

print()

with open(caminho,'r') as arquivo:
    print(arquivo.read())