import math

figure = input()
area = None

if figure == 'square':
    side_a = float(input())
    area = side_a ** 2
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == 'circle':
    side_a = float(input())
    area = math.pi * side_a ** 2
elif figure == 'triangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b / 2

print(round(area, 3))
