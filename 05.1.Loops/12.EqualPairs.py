n = int(input())
previous_value = None
diff = 0
max_diff = None
is_same = True


def get_max_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# diff and maxdiff not working!
# https://python-book.softuni.bg/chapter-05-loops.html
# https://judge.softuni.bg/Contests/Practice/Index/1053#11

for i in range(0, n):
    first_number = int(input())
    second_number = int(input())
    pair_sum = first_number + second_number
    if previous_value:
        if previous_value != pair_sum:
            is_same = False
            diff = abs(pair_sum - previous_value)
            print('diff: ', diff)
            print('pair_sum', pair_sum)
            print('previous_sum', previous_value)
            if diff > max_diff:
                max_diff = diff
        # print('diff: ', diff)
        # print('max_diff: ', max_diff)
    else:
        previous_value = pair_sum
        max_diff = diff

print(max_diff)
print(f'Yes, value={pair_sum}' if is_same else f'No, maxdiff=')
