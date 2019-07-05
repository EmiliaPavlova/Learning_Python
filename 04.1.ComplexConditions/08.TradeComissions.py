city = input()
sales = float(input())

ranges = None
if 0 <= sales <= 500:
    ranges = 0
elif sales <= 1000:
    ranges = 1
elif sales <= 10000:
    ranges = 2
elif sales > 10000:
    ranges = 3

commissions = {
    'Sofia': {0: 5/100, 1: 7/100, 2: 8/100, 3: 12/100},
    'Varna': {0: 4.5/100, 1: 7.5/100, 2: 10/100, 3: 13/100},
    'Plovdiv': {0: 5.5/100, 1: 8/100, 2: 12/100, 3: 14.5/100}
}

try:
    print(round(commissions.get(city).get(ranges) * sales, 2) if sales > 0 else 'error')
except:
    print('error')
