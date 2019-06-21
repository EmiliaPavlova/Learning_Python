import math

rad = float(input('Enter radians: '))


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return round(num)


deg = format_number(rad * 180 / math.pi)
print(f'In degrees: {deg}')
