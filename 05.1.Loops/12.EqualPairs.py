n = int(input())
previous_value = None
diff = 0
max_diff = 0
is_same = True


def get_max_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


for i in range(0, n):
    first_number = int(input())
    second_number = int(input())
    pair_sum = first_number + second_number

    if previous_value:
        if previous_value != pair_sum:
            is_same = False
            diff = abs(pair_sum - previous_value)
            max_diff = get_max_number(max_diff, diff)
    previous_value = pair_sum

print(f'Yes, value={pair_sum}' if is_same else f'No, maxdiff={max_diff}')
