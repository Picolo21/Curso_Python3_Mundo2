# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o

sum = 0
count = 1

for c in range(0, 6):
    value = int(input(f'Digite o {count}º número inteiro: '))
    if (value % 2 == 0):
        sum += value
    count += 1

print(f'A soma de todos os números pares digitados é igual a {sum}')
