# Faça um programa que leia um número inteiro qualquer e mostre o seu fatorial

# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

value = int(input('Digite um número inteiro qualquer para calcular seu Fatorial: '))

fatorial = 1

print(f'\nCalculando {value}! = ', end='')

while (value > 0):
    print(f'{value}', end='')
    print(' x ' if value > 1 else ' = ', end='')
    fatorial *= value
    value -= 1

print(f'{fatorial}')
