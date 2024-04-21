# Faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de 3 e que se encontram no intervalo de 1 até 500

count = 0
sum = 0

for c in range(1, 501):
    if ((c % 2 != 0) and (c % 3 == 0)):
        count += 1
        sum += c

print(f'A soma dos {count} números impares múltiplos de 3 é igual a {sum}')
