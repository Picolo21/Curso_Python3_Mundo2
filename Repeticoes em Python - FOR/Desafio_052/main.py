# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

value = int(input('Digite um número inteiro qualquer: '))
count = 0

for c in range(1, (value + 1)):
    if ((value % c) == 0):
        count += 1

if (count == 2):
    print(f'O número {value} É PRIMO')
else:
    print(f'O número {value} NÃO É PRIMO')
