# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numbers_count = 0
numbers_sum = 0

value = int(input('Digite um número [999 para parar]: '))

while (value != 999):
    numbers_count += 1
    numbers_sum += value
    value = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {numbers_count} número(s) e a soma entre eles foi {numbers_sum}.')
