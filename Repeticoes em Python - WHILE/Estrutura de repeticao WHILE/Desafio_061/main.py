# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma P.A., mostrando
# os 10 primeiros termos da progressão usando a estrutura WHILE

first_value = int(input('Primeiro termo: '))
second_value = int(input('Razão da PA: '))

count = 1

while (count <= 10):
    print(f'{first_value}', end='')
    print(' -> ', end='')
    count += 1
    first_value += second_value

print('FIM')
