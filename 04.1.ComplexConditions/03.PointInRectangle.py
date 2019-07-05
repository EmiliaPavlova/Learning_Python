x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

inside_x = x1 <= x <= x2
inside_y = y1 <= y <= y2

print('Inside' if inside_x and inside_y else 'Outside')
