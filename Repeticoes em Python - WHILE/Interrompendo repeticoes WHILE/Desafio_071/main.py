# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues

# OBS: Considere que o caixa possui cédula de R$ 50, R$ 20, R$ 10 e R$ 1.

import math

money_notes_of_50 = 0
money_notes_of_20 = 0
money_notes_of_10 = 0
money_notes_of_1 = 0

print('=' * 35)
print(' ' * 12, 'BANCO CEV')
print('=' * 35, end='\n\n')

value = int(input('Qual o valor você gostaria de sacar? R$ '))

while True:
    if (value > 50):
        money_notes_of_50 = math.floor(value / 50)
        rest = value % 50
        print(f'Total de {money_notes_of_50} notas de R$ 50,00')

    if ((value - (money_notes_of_50 * 50)) > 20):
        money_notes_of_20 = math.floor(rest / 20)
        rest = rest % 20
        print(f'Total de {money_notes_of_20} notas de R$ 20,00')

    if ((value - (money_notes_of_50 * 50) - (money_notes_of_20 * 20)) > 10):
        money_notes_of_10 = math.floor(rest / 10)
        rest = rest % 10
        print(f'Total de {money_notes_of_10} notas de R$ 10,00')

    if ((value - (money_notes_of_50 * 50) - (money_notes_of_20 * 20) - (money_notes_of_10 * 10)) > 0):
        money_notes_of_1 = rest / 1
        print(f'Total de {money_notes_of_1:.0f} notas de R$ 1,00')

    break

print('=' * 50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
