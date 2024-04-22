# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

# OBS: Considere maior de idade a partir de 21 anos de idade

from datetime import date

adult = 0
underage = 0

for person in range(0, 7):
    birth = int(input(f'Em que ano a {person + 1}ª pessoa nasceu? '))
    actual = date.today().year
    age = actual - birth
    if (age >= 21):
        adult += 1
    else:
        underage += 1

print(f'\nAo todo tivemos {adult} pessoas maiores de idade e {underage} pessoas menores de idade')
