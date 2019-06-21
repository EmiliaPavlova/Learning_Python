dollars = float(input('Enter USD: '))


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return round(num, 2)


leva = format_number(dollars * 1.79549)
print(f'In BGN: {leva}')
