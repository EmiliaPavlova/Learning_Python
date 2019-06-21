x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

x = abs(x1 - x2)
y = abs(y1 - y2)
area = x * y
perimeter = 2 * (x + y)


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


print(f'The rectangle area is {format_number(area)}')
print(f'The rectangle perimeter is {format_number(perimeter)}')
