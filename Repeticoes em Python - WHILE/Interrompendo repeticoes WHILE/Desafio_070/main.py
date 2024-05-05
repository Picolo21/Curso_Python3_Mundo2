# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$ 1.000,00
# C) Qual é o nome do produto mais barato

total = 0
cheapest_product_name = ''
cheapest_product_price = 0
more_expensive_products = 0

print('=' * 42)
print(' ' * 11, 'LOJA SUPER BARATÃO')
print('=' * 42)

while True:
    product_name = input('Nome do produto: ')
    product_price = float(input('Preço: '))
    if (product_price > 1000):
        more_expensive_products += 1
    if (cheapest_product_price == 0):
        cheapest_product_name = product_name
        cheapest_product_price = product_price
    if (cheapest_product_price > product_price):
        cheapest_product_name = product_name
        cheapest_product_price = product_price
    total += product_price
    option = input('Quer continuar [S / N]? ').upper()
    if (option == 'N'):
        break

print()
print('-' * 25, 'FIM DO PROGRAMA', '-' * 25, end='\n\n')
print(f'O total da compra foi de R$ {total:,.2f}')
print(f'Temos {more_expensive_products} produto(s) custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {cheapest_product_name} que custou R$ {cheapest_product_price:.2f}')
