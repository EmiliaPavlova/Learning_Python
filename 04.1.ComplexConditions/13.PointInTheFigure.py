h = int(input())
x = float(input())
y = float(input())

x1_1 = 0
y1_1 = 0
x2_1 = 3 * h
y2_1 = 1 * h
is_inside_1 = (x1_1 < x < x2_1) and (y1_1 < y < y2_1)
is_on_border_1 = (y1_1 <= y <= y2_1 and (x == x1_1 or x == x2_1) or
                  x1_1 <= x <= x2_1 and (y == y1_1 or y == y2_1))

x1_2 = 1 * h
y1_2 = 0
x2_2 = 2 * h
y2_2 = 4 * h
is_inside_2 = (x1_2 < x < x2_2) and (y1_2 < y < y2_2)
is_on_border_2 = (y1_2 <= y <= y2_2 and (x == x1_2 or x == x2_2) or
                  x1_2 <= x <= x2_2 and (y == y1_2 or y == y2_2))

result = ''
if is_inside_1 or is_inside_2:
    result = 'inside'
elif is_on_border_1 or is_on_border_2:
    result = 'border'
else:
    result = 'outside'
print(result)
