# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:

# Abaixo de 18,5: Abaixo do peso
# Entre 18,5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida

print(f'{'='*56}')
print(f'{'':20} CÁLCULO DE IMC ')
print(f'{'='*56}', end='\n\n')

weight = float(input('Informe seu peso (Kg): '))
height = float(input('Informe sua altura (m): '))

imc = weight / (height ** 2)

print(f'\nO IMC dessa pessoa é de {imc:.2f}')

if (imc < 18.5):
    print('Você está ABAIXO DO PESO normal')
elif (imc < 25):
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif (imc < 30):
    print('Você está com SOBREPESO')
elif (imc < 40):
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
