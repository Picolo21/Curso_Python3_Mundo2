# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

gender = input('Informe seu sexo [ M / F ]: ').upper()

while ((gender != 'M') and (gender != 'F')):
    gender = input('Dados inválidos. Por favor, informe seu sexo novamente [ M / F ]: ').upper()

print(f'Sexo {gender} registrado com sucesso!')
