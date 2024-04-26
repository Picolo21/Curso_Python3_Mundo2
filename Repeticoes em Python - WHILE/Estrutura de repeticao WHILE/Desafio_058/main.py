# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''', end='\n\n')

count = 1
computer_value = randint(0, 10)

player_value = int(input('Qual seu palpite? '))

while (computer_value != player_value):
    if (computer_value > player_value):
        print('Mais... Tente mais uma vez')
        player_value = int(input('Qual seu palpite? '))
        count += 1
    elif (computer_value < player_value):
        print('Menos... Tente mais uma vez')
        player_value = int(input('Qual seu palpite? '))
        count += 1
    else:
        count += 1

print(f'Acertou com {count} tentativas. Parabéns!')
