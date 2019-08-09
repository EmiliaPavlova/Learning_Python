count_of_loads = int(input())
microbus_limit = 3
microbus_price = 200
truck_limit = 11
truck_price = 175
train_price = 120
microbuses_sum = 0
trucks_sum = 0
trains_sum = 0
sum_of_loads = 0

for i in range(1, count_of_loads + 1):
    load = int(input())
    sum_of_loads += load
    if load <= microbus_limit:
        microbuses_sum += load
    elif load <= truck_limit:
        trucks_sum += load
    else:
        trains_sum += load


def format_result(num, sum_numbers):
    return f'{num / sum_numbers * 100:.2f}%'


print(f'{(microbuses_sum * microbus_price + trucks_sum * truck_price + trains_sum * train_price) / sum_of_loads:.2f}')
print(format_result(microbuses_sum, sum_of_loads))
print(format_result(trucks_sum, sum_of_loads))
print(format_result(trains_sum, sum_of_loads))
