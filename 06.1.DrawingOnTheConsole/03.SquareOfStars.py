n = int(input())
for row in range(n):
    print('*', end='')
    for col in range(1, n):
        print(' *', end='')
    print()
