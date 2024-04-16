# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

birth_year = int(input('Informe o ano de nascimento do atleta: '))

actual_year = date.today().year
age = actual_year - birth_year

print(f'\nO atleta tem {age} anos.')

if (age <= 9):
    print('Classificação: MIRIM')
elif (age <= 14):
    print('Classificação: INFANTIL')
elif (age <= 19):
    print('Classificação: JÚNIOR')
elif (age <= 25):
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
