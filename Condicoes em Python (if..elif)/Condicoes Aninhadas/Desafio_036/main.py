# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador  e em quantos anos
# ele vai pagar

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
# então o empréstimo será negado

home_price = float(input('Informe o valor da casa que deseja comprar: R$ '))
salary = float(input('Informe o valor do seu salário: R$ '))
quantity_of_months = int((input('Informe em quantos meses deseja pagar o empréstimo: ')))

percentage_loan_installment_limit = salary * 0.3

loan_installment = home_price / quantity_of_months

if (loan_installment > percentage_loan_installment_limit):
    print(f'\nPara pagar uma casa de R$ {home_price:.2f} em {quantity_of_months} meses, a prestação será de R$ {loan_installment:.2f}')
    print('Empréstimo NEGADO')
else:
    print(f'\nPara pagar uma casa de R$ {home_price:.2f} em {quantity_of_months} meses, a prestação será de R$ {loan_installment:.2f}')
    print('Empréstimo APROVADO')
