n = int(input())
left_sum = 0
right_sum = 0
for i in range(0, n):
    left_sum += int(input())
for i in range(n, 2 * n):
    right_sum += int(input())
print(f'Yes, sum = {left_sum}'
      if left_sum == right_sum
      else f'No, diff = {abs(left_sum - right_sum)}')