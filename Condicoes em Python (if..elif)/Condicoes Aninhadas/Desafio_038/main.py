# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
# uma das seguintes mensagens:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois números são iguais

value_first = int(input('Informe o 1º valor: '))
value_second = int(input('Informe o 2º valor: '))

if (value_first > value_second):
    print('\nO primeiro valor é maior')
elif (value_second > value_first):
    print('\nO segundo valor é maior')
else:
    print('\nNão existe valor maior, os dois números são iguais')
