# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do programa

from time import sleep

value_first = float(input('Informe o 1º valor: '))
value_second = float(input('Informe o 2º valor: '))

print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''', end='\n\n')

option = int(input('Qual é a sua opção? '))

while (option != 5):
    if (option == 1):
        sum = value_first + value_second
        print(f'A soma entre {value_first} e {value_second} é {sum:.2f}')
        print()
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa', end='\n\n')

        option = int(input('Qual é a sua opção? '))
    elif (option == 2):
        multiplication = value_first * value_second
        print(f'A multiplicação entre {value_first} e {value_second} é {multiplication:.2f}')
        print()
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa', end='\n\n')

        option = int(input('Qual é a sua opção? '))
    elif (option == 3):
        greater = 0
        if (value_first > value_second):
            greater = value_first
            print(f'Entre {value_first} e {value_second}, {greater} é o maior')
        elif (value_first < value_second):
            greater = value_second
            print(f'Entre {value_first} e {value_second}, {greater} é o maior')
        else:
            print(f'Entre {value_first} e {value_second}, os dois tem o mesmo valor')
        print()
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa', end='\n\n')

        option = int(input('Qual é a sua opção? '))
    elif (option == 4):
        value_first = float(input('Informe o 1º valor: '))
        value_second = float(input('Informe o 2º valor: '))

        print()
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa', end='\n\n')

        option = int(input('Qual é a sua opção? '))
    else:
        print('Opção inválida. Por favor, insira uma opção válida')
        print()
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa', end='\n\n')

        option = int(input('Qual é a sua opção? '))

print('\nSaindo do programa...')
sleep(3)
print('Programa finalizado!')
