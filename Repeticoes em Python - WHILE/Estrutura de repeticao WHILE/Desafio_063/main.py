# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma Sequência Fibonacci

print('='*50)
print(' '*13, 'SEQUÊNCIA DE FIBONACCI')
print('='*50)

value = int(input('Quantos termos você quer mostrar? '))

value_first = 0
value_second = 1

count = 2

print(f'{value_first} -> {value_second} -> ', end='')
while (count < value):
    value_third = value_first + value_second
    print(f'{value_third}', end='')
    print(' -> ', end='')
    count += 1
    value_first = value_second
    value_second = value_third

print('FIM')
