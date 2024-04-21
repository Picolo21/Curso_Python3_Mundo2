# Crie um programa que mostre na tela todos os números pares que
# estão no intervalo entre 1 e 50

cont = 1

for c in range(1, 51):
    if (c % 2 == 0):
        print(f'{cont}º = {c}')
        cont += 1

print('Acabou!')
