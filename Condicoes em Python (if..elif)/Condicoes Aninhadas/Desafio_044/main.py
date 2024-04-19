# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:

# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print(f'{'='*57}')
print(f'{'':20} LOJAS GUANABARA ')
print(f'{'='*57}', end='\n\n')

value = float(input('Preço das comprar: R$ '))
print(f'\n{'-'*57}')

print(f'''
FORMAS DE PAGAMENTO:

[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (até 12x)''', end='\n\n')

payment_option = int(input('Qual a opção de pagamento? '))

if (payment_option == 1):
    total = value - (value * 0.1)
    print(f'Sua compra de R$ {value:.2f} vai custar R$ {total:.2f}')
elif (payment_option == 2):
    total = value - (value * 0.05)
    print(f'Sua compra de R$ {value:.2f} vai custar R$ {total:.2f}')
elif (payment_option == 3):
    total = value
    print(f'Sua compra de R$ {value:.2f} vai custar R$ {total:.2f} em 2x de {(total / 2.0):.2f}')
elif (payment_option == 4):
    number_of_installments = int(input('Quantas parcelas deseja dividir sua compra? '))
    if (number_of_installments <= 12):
        total = value + (value * 0.2)
        print(f'Sua compra de R$ {value:.2f} vai custar R$ {total:.2f} em {number_of_installments}x de R$ {(total / number_of_installments):.2f}')
    else:
        print('Desculpe, só podemos dividir em até 12x')
else:
    print('Infelizmente você optou por uma opção inválida :(')
