# Escreve um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão:

# 1 para BINÁRIO
# 2 para OCTAL
# 3 para HEXADECIMAL

number = int(input('Escolha um número inteiro: '))

print('''\nEscolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

option = int(input('\nSua opção: '))

if (option == 1):
    print(f'\n{number} convertido para BINÁRIO é igual a {bin(number)[2:]}')
elif (option == 2):
    print(f'\n{number} convertido para OCTAL é igual a {oct(number)[2:]}')
elif (option == 3):
    print(f'\n{number} convertido para HEXADECIMAL é igual a {hex(number)[2:]}')
else:
    print('\nVocê escolheu uma opção inválida :(')
