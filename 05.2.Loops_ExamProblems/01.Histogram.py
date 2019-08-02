n = int(input())
p1_range = 200
p2_range = 400
p3_range = 600
p4_range = 800
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    number = int(input())
    if number < p1_range:
        p1 += 1
    elif number < p2_range:
        p2 += 1
    elif number < p3_range:
        p3 += 1
    elif number < p4_range:
        p4 += 1
    else:
        p5 += 1

sum_p = p1 + p2 + p3 + p4 + p5


def format_result(num, sum_p):
    return f'{num / sum_p * 100:.2f}%'


print(format_result(p1, sum_p))
print(format_result(p2, sum_p))
print(format_result(p3, sum_p))
print(format_result(p4, sum_p))
print(format_result(p5, sum_p))

