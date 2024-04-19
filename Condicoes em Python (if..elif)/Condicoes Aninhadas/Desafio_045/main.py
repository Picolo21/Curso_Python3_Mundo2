# Crie uma programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

print('''Suas opções:

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''', end='\n\n')

option = int(input('Qual é a sua escolha? '))

items = ('Pedra', 'Papel', 'Tesoura')
computer = randint(1, 3)

print('=' *50)

if ((option < 1) or (option > 3)):
    result = 'Jogada inválida :('
elif (option == 1):
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!', end='\n\n')
    print(f'O computador jogou {items[(computer - 1)]}')
    print(f'O jogador jogou {items[(option - 1)]}', end='\n\n')
    if (computer == 1):
        result = 'Resultado: EMPATE'
    elif (computer == 2):
        result = 'Resultado: COMPUTADOR VENCE'
    else:
        result = 'Resultado: JOGADOR VENCE'
elif (option == 2):
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!', end='\n\n')
    print(f'O computador jogou {items[(computer - 1)]}')
    print(f'O jogador jogou {items[(option - 1)]}', end='\n\n')
    if (computer == 1):
        result = 'Resultado: JOGADOR VENCE'
    elif (computer == 2):
        result = 'Resultado: EMPATE'
    else:
        result = 'Resultado: COMPUTADOR VENCE'
elif (option == 3):
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!', end='\n\n')
    print(f'O computador jogou {items[(computer - 1)]}')
    print(f'O jogador jogou {items[(option - 1)]}', end='\n\n')
    if (computer == 1):
        result = 'Resultado: COMPUTADOR VENCE'
    elif (computer == 2):
        result = 'Resultado: JOGADOR VENCE'
    else:
        result = 'Resultado: EMPATE'

print(result)

print('=' *50)
