"""palavra = 'acido'
tentativas = 0
asteristico = '*****'
resposta = ''

while True:
    letra = input('escolha uma letra: ')

    if len(letra) != 1:
        print('Apenas uma letra')
        continue
 

    if letra in 'acido':
        print(f'A letra "{letra}" está na palavra')
        for c in palavra:
            asteristico 
            if c == letra:
                asteristico += letra
                if asteristico != '*':
                    resposta += letra
                
                print(asteristico,end='')
            else:
                print(asteristico,end='')


    else:
        print('Essa letra não está na palavra')
        print('palavra:',len(palavra)* '*')

    escolha = input('Deseja falar a palavra completa[S/N]? ').upper()

    if escolha == 'S':
        chute = input('Qual a palavra? ')
        if chute == palavra:
            break
        else:
            print('Você errou!')




    tentativas +=1


print('Você ganhou o jogo') """

"""Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0