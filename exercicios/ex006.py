frase = 'O python foi criado por mim,esquça tudo, se eu sou pai do python porque ele não me obedece?'.lower()
contagem = 0
#letra_p = 0

#while contagem < len(frase):
 #   frase[contagem]
  #  if frase[contagem] == 'p':
   #     letra_p+=1
    #contagem +=1

#print(f'Foi encontrado {letra_p} letra p')

letra_mais_vezes = ''
qntd_vezes1 = 0

while contagem < len(frase):
    letra_atual = frase[contagem]
    Quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        contagem+=1
        continue

    if qntd_vezes1 < Quantas_vezes_letra_apareceu:
        qntd_vezes1 = Quantas_vezes_letra_apareceu
        letra_mais_vezes = letra_atual
    contagem+=1
print(f'A letra {letra_mais_vezes} apareceu mais vezes, apareceu {qntd_vezes1} vezes')