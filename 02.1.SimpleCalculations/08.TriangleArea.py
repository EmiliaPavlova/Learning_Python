a = float(input('Enter side: '))
h = float(input('Enter height: '))

area = a * h / 2


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return round(num, 2)


print(f'Triangle area = {format_number(area)}')
