x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

border_x = y1 <= y <= y2 and (x == x1 or x == x2)
border_y = x1 <= x <= x2 and (y == y1 or y == y2)

print('Border' if border_x or border_y else 'Inside / Outside')
