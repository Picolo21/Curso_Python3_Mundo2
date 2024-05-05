# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa enecerra quando ele disser que quer mostrar 0 termos.

first_value = int(input('Primeiro termo: '))
second_value = int(input('Razão da PA: '))

count = 1
sum = 10

while (count <= 10):
    print(first_value, end='')
    print(' -> ', end='')
    first_value += second_value
    count += 1
    print('PAUSA\n' if (count > 10) else '', end='')
    if (count > 10):
        count_second = 1
        while (count_second != 0):
            count_second = int(input('Quantos termos você quer mostrar a mais? '))
            sum += count_second
            if (count_second != 0):
                count_third = count_second
                while (count_third != 0):
                    print(first_value, end='')
                    print(' -> ', end='')
                    first_value += second_value
                    count_third -= 1
                    print('PAUSA\n' if count_third == 0 else '', end='')

print(f'Progressão finalizada com {sum} termos mostrados.')

