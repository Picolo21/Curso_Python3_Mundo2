# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

people_over_18_years_old = 0
men = 0
women_under_20_years_old = 0

print('=' * 33)
print(' '*6, 'CADASTRO DE PESSOAS')
print('=' * 33, end='\n\n')

while True:
    print('-' * 33)
    print(' '*6, 'CADASTRE UMA PESSOA')
    print('-' * 33)
    age = int(input('Idade: '))
    gender = input('Sexo [M / F]: ').upper()
    if (age > 18):
        people_over_18_years_old += 1
    if (gender == 'M'):
        men += 1
    if ((gender == 'F') and (age < 20)):
        women_under_20_years_old += 1
    print('-'*33)
    option = input('Quer continuar [S / N]? ').upper()
    if (option == 'N'):
        break

print(f'Total de pessoas com mais de 18 anos: {people_over_18_years_old}')
print(f'Ao todo, temos {men} homem(ns) cadastrado(s)')
print(f'E temos {women_under_20_years_old} mulher(es) com menos de 20 anos')
