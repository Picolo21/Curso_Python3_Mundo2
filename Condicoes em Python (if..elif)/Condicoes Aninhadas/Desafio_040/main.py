# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
# uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃo
# Média 7.0 ou superior: APROVADO

value_first = float(input('Digite o valor da 1ª nota: '))
value_second = float(input('Digite o valor da 2ª nota: '))

average = (value_first + value_second) / 2.0

print(f'\nTirando {value_first:.2f} e {value_second:.2f}, a média final do aluno é {average:.2f}')

if (average < 5.0):
    print('O aluno está REPROVADO')
elif (average < 7.0):
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
