import random
wins = 0
while True :

    print('Jogue par ou impar:')
    res = input('[1]Par [2]Impar: ')
    num1 = int(input('Agora, escolha um numero de 1 a 10: '))
    num2 = random.randint(1,10)
    print(f'O computador jogou {num2}')
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma} foi o numero sorteado')

    if soma % 2 == 0 :
        print('O numero é par')
        if res == 2 :
            wins += 1
            print('Você Ganhou!')
        else  :
            print('Você Perdeu!')
            break
    else :
        print('O numero é impar')
        if res == 1 :
            wins += 1
            print('Você Ganhou!')
        else :
            print('Você Perdeu!')
            break

print(f'Numero de vitorias: {wins}')
