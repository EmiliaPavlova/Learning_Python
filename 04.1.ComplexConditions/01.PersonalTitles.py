age = float(input())
gender = input()
address = None
if gender == 'm':
    if age < 16:
        address = 'Master'
    else:
        address = 'Mr.'
else:
    if age < 16:
        address = 'Miss'
    else:
        address = 'Ms.'
print(address)
