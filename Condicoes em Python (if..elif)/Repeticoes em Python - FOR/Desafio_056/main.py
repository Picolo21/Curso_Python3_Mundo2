# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

average = 0
man_name_old = ''
man_age_old = 0
women = 0
sum_age = 0

for person in range(0, 4):
    print(f'-'*5, f'{person + 1}ª PESSOA', f'-'*5)
    name = input('Nome: ')
    age = int(input('Idade: '))
    gender = input('Sexo [M / F]: ')
    print(f'-'*20, end='\n\n')
    sum_age += age
    if ((gender.upper() == 'M') and age > man_age_old):
        man_name_old = name
        man_age_old = age
    if ((gender.upper() == 'F') and age < 20):
        women += 1

average = sum_age / 4

print(f'\nA média de idade do grupo é de {average:.2f} anos')
print(f'O homem mais velho tem {man_age_old} anos e se chama {man_name_old}.')
print(f'Ao todo são {women} mulher(es) com menos de 20 anos')
