# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

first = float(input('Informe o valor do 1º segmento de reta: '))
second = float(input('Informe o valor do 2º segmento de reta: '))
third = float(input('Informe o valor do 3º segmento de reta: '))

if ((first < (second + third)) and (second < (first + third)) and (third < (first + second))):
    print('\nOs segmentos de reta acima PODEM FORMAR um triângulo ', end='')
    if (first == second == third):
        print('EQUILÁTERO!')
    elif ((first == second) or (first == third) or (second == third)):
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('\nOs segmentos de reta acima NÃO PODEM FORMAR um triângulo')
