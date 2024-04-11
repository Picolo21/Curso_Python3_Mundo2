# Faça um programa que leia o ano de um nascimento de um jovem e informe,
# de acordo com a sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento

# Seu programa também mostra o tempo que falta ou que passou do prazo

from datetime import date

now = date.today().year
birth = int(input('Informe o seu ano de nascimento: '))
age = now - birth

print(f'\nQuem nasceu em {birth} tem {age} anos em {now}')

if (age < 18):
    print(f'Ainda faltam {18 - age} anos para o alistamento')
    print(f'Seu alistamento será em {now + (18 - age)}')
elif (age == 18):
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {age - 18} anos')
    print(f'Seu alistamento foi em {now - (age - 18)}')
