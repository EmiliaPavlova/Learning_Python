prices = {
    'workday': {'banana': 2.50, 'apple': 1.20, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.70, 'pineapple': 5.50, 'grapes': 3.85},
    'weekend': {'banana': 2.70, 'apple': 1.25, 'orange': 0.90, 'grapefruit': 1.60, 'kiwi': 3.00, 'pineapple': 5.60, 'grapes': 4.20}
}
workday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

fruit = input()
day = input()
amount = float(input())

if day in workday:
    day = 'workday'
elif day in weekend:
    day = 'weekend'

try:
    print(round(prices.get(day, 'error').get(fruit, 'error') * amount, 2))
except:
    print('error')
