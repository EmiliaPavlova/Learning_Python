points = int(input())
bonus_points = None

if points > 1000:
    bonus_points = points * 0.1
elif points > 100:
    bonus_points = points * 0.2
else:
    bonus_points = 5

if points % 2 == 0:
    bonus_points += 1
elif points % 5 == 0:
    bonus_points += 2

print(bonus_points)
print(points + bonus_points)
