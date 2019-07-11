n = int(input())
odd_sum = 0
even_sum = 0
for i in range(0, n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
print(f'Yes\nSum = {odd_sum}'
      if odd_sum == even_sum
      else f'No\nDiff = {abs(odd_sum - even_sum)}')