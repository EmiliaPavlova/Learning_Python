number = int(input())
result = None

ones = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
tenths = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

if 0 > number or number > 100:
    result = 'invalid number'
elif int(number / 10) < 2:
    result = ones.get(number)
elif len(str(number)) == 2:
    result = tenths.get(int(number / 10)) + ' ' + ones.get(number % 10)\
        if number % 10 != 0\
        else tenths.get(int(number / 10))
else:
    result = 'one hundred'

print(result)
