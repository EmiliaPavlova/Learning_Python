month = input()
nights = int(input())

prices = {
    'apartment': {'May': 65, 'June': 68.7, 'July': 77, 'August': 77, 'September': 68.7, 'October': 65},
    'studio': {'May': 50, 'June': 75.2, 'July': 76, 'August': 76, 'September': 75.2, 'October': 50}
}

price_apartment = prices.get('apartment').get(month) * nights
price_studio = prices.get('studio').get(month) * nights

discount_apartment = 0
discount_studio = 0
if 7 < nights < 14 and (month == 'May' or month == 'October'):
    discount_studio = 0.05
elif nights > 14:
    discount_apartment = 0.1
    if month == 'May' or month == 'October':
        discount_studio = 0.3
    elif month == 'June' or month == 'September':
        discount_studio = 0.2

price_apartment -= discount_apartment * price_apartment
price_studio -= discount_studio * price_studio

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')
