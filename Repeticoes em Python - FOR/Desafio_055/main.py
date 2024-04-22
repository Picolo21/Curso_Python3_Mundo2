# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.

bigger = 0
smaller = 0

for person in range(0, 5):
    weight = float(input(f'Qual o peso da {person + 1}ª pessoa? '))
    if (person == 0):
        bigger = weight
        smaller = weight
    if (bigger < weight):
        bigger = weight
    if (smaller > weight):
        smaller = weight

print(f'\nO maior peso lido foi de {bigger:.2f} Kg')
print(f'O menor peso lido foi de {smaller:.2f} Kg')
