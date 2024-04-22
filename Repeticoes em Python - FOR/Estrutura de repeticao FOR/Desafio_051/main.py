# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.. No final,
# mostre os 10 primeiros termos dessa progressão

initial_value = int(input('Informe um número inteiro qualquer que deseja iniciar a P.A.: '))
value = int(input('Informe o valor da razão: '))

for c in range(0, 10):
    print(f'{initial_value}', end='')
    print(' -> ', end='')
    initial_value += value

print('FIM')
