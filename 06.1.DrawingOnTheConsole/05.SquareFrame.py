n = int(input())

# top row
print('+', end='')
for i in range(n - 2):
    print(' -', end='')
print(' +')

# middle rows
for row in range(n - 2):
    print('|', end='')
    for col in range(n - 2):
        print(' -', end='')
    print(' |')

# bottom row
print('+', end='')
for i in range(n - 2):
    print(' -', end='')
print(' +')
