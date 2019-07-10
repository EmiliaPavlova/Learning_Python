budget = float(input())
category = input()
count = int(input())
transport = 0
price_vip = 499.99
price_normal = 249.99

if count < 5:
    transport = 0.75
elif count < 10:
    transport = 0.6
elif count < 25:
    transport = 0.5
elif count < 50:
    transport = 0.4
else:
    transport = 0.25
budget -= budget * transport

tickets = count * (price_vip if category == 'VIP' else price_normal)
result = budget - tickets
print(f'Yes! You have {result:.2f} leva left.'
      if result >= 0
      else f'Not enough money! You need {abs(result):.2f} leva.')
