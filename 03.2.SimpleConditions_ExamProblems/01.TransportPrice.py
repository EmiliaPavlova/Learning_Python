km = int(input())
daytime = input()

taxi_day = 0.7 + 0.79 * km
taxi_night = 0.7 + 0.9 * km
bus = 0.09 * km
but_range = 20
train = 0.06 * km
train_range = 100

lowest_price = None

if km >= 100:
    lowest_price = train
elif km >= 20:
    lowest_price = bus
else:
    lowest_price = taxi_day if daytime == 'day' else taxi_night

print(lowest_price)
