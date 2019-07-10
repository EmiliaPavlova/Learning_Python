number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
output = f'{number_1} {operator} {number_2} = '

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    output += f'{result} - '
    output += 'even' if result % 2 == 0 else 'odd'
elif operator == '/' or operator == '%':
    if number_2 == 0:
        output = f'Cannot divide {number_1} by zero'
    elif operator == '/':
        result = number_1 / number_2
        output += f'{result:.2f}'
    else:
        output += f'{number_1 % number_2}'

print(output)
