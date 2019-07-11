from sys import maxsize

n = int(input())
sum_all = 0
biggest_number = -maxsize
for i in range(0, n):
    number = int(input())
    sum_all += number
    if biggest_number < number:
        biggest_number = number
has_match = sum_all / 2 == biggest_number

print(f'Yes\nSum = {biggest_number}'
      if has_match
      else f'No\nDiff = {abs(sum_all - 2 * biggest_number)}')
