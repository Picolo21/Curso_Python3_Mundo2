# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores

numbers_count = 0
numbers_sum = 0
average = 0
bigger = smaller = 0
option = 'S'

while (option != 'N'):
    value = int(input('Digite um número: '))
    option = input('Quer continuar [S / N]? ').upper()
    if (numbers_count == 0):
        bigger = smaller = value
    if (value > bigger):
        bigger = value
    if (value < smaller):
        smaller = value
    numbers_sum += value
    numbers_count += 1

average = numbers_sum / numbers_count

print(f'Você digitou {numbers_count} número(s) e a média foi de {average:.2f}')
print(f'O maior valor foi {bigger} e o menor foi {smaller}')
