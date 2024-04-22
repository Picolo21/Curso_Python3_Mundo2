# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# desconsiderando os espaços. OBS: não use acentuação na frase

count_one = 0
text = input('Digite uma frase qualquer: ')
new_text = text.replace(' ', '')

if ((len(new_text) % 2) == 0):
    count_two = len(new_text)
    for c in range(0, (int)((len(new_text) + 1) / 2)):
        if (new_text[c] == new_text[count_two - 1]):
            count_one += 1
            count_two -= 1
else:
    count_two = len(new_text)
    for c in range(0, (int)((len(new_text) - 1) / 2)):
        if (new_text[c] == new_text[count_two - 1]):
            count_one += 1
            count_two -= 1

if (((len(new_text) % 2) == 0) and (count_one == (len(new_text) / 2))):
    print('A frase digitada É UM PALÍNDROMO')
elif (((len(new_text) % 2) == 0) and (count_one != (len(new_text) / 2))):
    print('A frase digitada NÃO É UM PALÍNDROMO')
elif (((len(new_text) % 2) != 0) and (count_one == ((len(new_text) - 1) / 2))):
    print('A frase digitada É UM PALÍNDROMO')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO')
