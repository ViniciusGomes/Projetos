lista = ('Hamburger', 10.8, 'Suco', 12.5, 'Pizza', 24.9, 'Pudim', 9.9)

for each in range(0, len(lista), 2):
    print(f'{lista[each]:.<10} R$ {lista[each+1]:>5.2f}')
