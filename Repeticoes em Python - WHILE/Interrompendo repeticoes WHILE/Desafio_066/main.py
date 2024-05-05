# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numbers_count = 0
numbers_sum = 0

while True:
    value = int(input('Digite um valor [999 para parar]: '))
    if (value == 999):
        break
    numbers_count += 1
    numbers_sum += value

print(f'A soma do(s) {numbers_count} valor(es) foi {numbers_sum}!')
