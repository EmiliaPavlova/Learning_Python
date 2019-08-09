n = int(input())

# upper part
for row in range(n):
    print(' ' * (n - row - 1), end='')
    print('*', end='')
    for col in range(row):
        print(' *', end='')
    print()

# bottom part
for row in range(n - 1):
    for col in range(row):
        print(' ', end='')
    for col in range(n - row - 1):
        print(' *', end='')
    print()
