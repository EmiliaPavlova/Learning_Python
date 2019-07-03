number = int(input())
first_check = 100
second_check = 200

if number < first_check:
    print(f'Less than {first_check}')
elif first_check <= number <= second_check:
    print(f'Between {first_check} and {second_check}')
else:
    print(f'Greater than {second_check}')
