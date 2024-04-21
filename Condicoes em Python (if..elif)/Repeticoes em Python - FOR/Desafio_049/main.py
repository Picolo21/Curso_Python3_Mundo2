# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço FOR

value = int(input('Digite um valor que deseja saber a tabuada: '))

print(f'\nTabuada do {value}:', end='\n\n')

for c in range(0, 11):
    total = value * c
    print(f'{value} X {c} = {total}')
