while True :
    num = int(input('Digite um numero: '))

    if num < 0:
        print('Fim')
        break

    else:
        print(f'Tabuada do {num}')

        for tabuada in range(1,11):
            var = num * tabuada
            print(f'{num} X {tabuada} = {var}')
