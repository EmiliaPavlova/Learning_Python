n = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(0, n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

sum_p = p1 + p2 + p3


def format_result(num, sum_numbers):
    return f'{num / sum_numbers * 100:.2f}%'


print(format_result(p1, n))
print(format_result(p2, n))
print(format_result(p3, n))
