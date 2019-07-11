from sys import maxsize

n = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if even_min > number:
            even_min = number
        if even_max < number:
            even_max = number
    else:
        odd_sum += number
        if odd_min > number:
            odd_min = number
        if odd_max < number:
            odd_max = number


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


if odd_min == maxsize:
    odd_min = 'No'
else:
    odd_min = format_number(odd_min)
if odd_max == -maxsize:
    odd_max = 'No'
else:
    odd_max = format_number(odd_max)
if even_min == maxsize:
    even_min = 'No'
else:
    even_min = format_number(even_min)
if even_max == -maxsize:
    even_max = 'No'
else:
    even_max = format_number(even_max)

print(f'OddSum={format_number(odd_sum)}\n'
      f'OddMin={odd_min}\n'
      f'OddMax={odd_max}\n'
      f'EvenSum={format_number(even_sum)}\n'
      f'EvenMin={even_min}\n'
      f'EvenMax={even_max}')
