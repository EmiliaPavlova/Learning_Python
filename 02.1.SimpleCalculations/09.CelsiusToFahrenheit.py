c = float(input('Enter degree in Celsius: '))


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return round(num, 2)


f = format_number(c * 9 / 5 + 32)
print(f'In Fahrenheit: {f}')
