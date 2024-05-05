# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo

from random import randint

count = 0

print('=' * 34)
print(' '*4, 'VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 34, end='\n\n')

while True:
    player = int(input('Diga um valor: '))
    option = input('Par ou ímpar [P / I]? ').upper()
    computer = randint(0, 10)
    total = player + computer
    print('=' * 50)
    if ((total % 2 == 0) and (option == 'P')):
        print(f'Você jogou {player} e o computador {computer}. Total de {total} DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
        print('=' * 50)
    if ((total % 2 == 0) and (option == 'I')):
        print(f'Você jogou {player} e o computador {computer}. Total de {total} DEU PAR')
        print('Você PERDEU!')
        print('=' * 50)
        break
    if ((total % 2 != 0) and (option == 'P')):
        print(f'Você jogou {player} e o computador {computer}. Total de {total} DEU ÍMPAR')
        print('Você PERDEU!')
        print('=' * 50)
        break
    if ((total % 2 != 0) and (option == 'I')):
        print(f'Você jogou {player} e o computador {computer}. Total de {total} DEU ÍMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
        print('=' * 50)

print(f'GAME OVER! Você venceu {count} vez(es) seguida(s)')
