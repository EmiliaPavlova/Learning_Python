lilly_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

birthday_amount = 10
money_received = 0
toys_received = 0

for lilly_age in range(1, lilly_age + 1):
    if lilly_age % 2 == 0:
        money_received += birthday_amount - 1
        birthday_amount += 10
    else:
        toys_received += 1

money_received += toys_received * toy_price
money_difference = money_received - washing_machine_price

print(f'Yes! {money_difference:.2f}' if money_difference >= 0 else f'No! {abs(money_difference):.2f}')
