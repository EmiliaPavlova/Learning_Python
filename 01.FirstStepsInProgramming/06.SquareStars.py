print("Enter a number:")
a = int(input())
if a >= 2:
    for i in range(1, a + 1):
        if i != 1 and i != a:
            # print('*' + (' ' * (a - 2)) + '*')
            print(f'*{" " * (a - 2)}*')
        else:
            print('*' * a)
else:
    print("The number should be bigger or equal to 2")
