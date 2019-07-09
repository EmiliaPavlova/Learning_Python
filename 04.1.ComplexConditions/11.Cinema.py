type_projection = input()
rows = int(input())
columns = int(input())

prices = {'Premiere': 12, 'Normal': 7.5, 'Discount': 5}

print(f'{round(rows * columns * prices.get(type_projection), 2)} leva')
