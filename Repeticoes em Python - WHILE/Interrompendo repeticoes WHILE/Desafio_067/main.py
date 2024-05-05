# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    value = int(input('Quer ver a tabuada de qual valor? '))
    if (value < 0):
        break
    print('=' * 25)
    for count in range(0, 11):
        print(f'{value} X {count} = {value * count}')
    print('=' * 25)

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
