import os

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
        ('linha 3\n','linha 4\n')
    )

print()

with open(caminho,'a') as arquivo:
    arquivo.write('É us gu')


with open(caminho,'r') as arquivo:
    print(arquivo.read()) 

# os.unlink(caminho) Apaga o arquivo
os.rename(caminho,'outro_nome')

