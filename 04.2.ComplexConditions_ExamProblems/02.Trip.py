budget = float(input())
season = input()

plan = {
    'summer': {'Bulgaria': 0.3, 'Balkans': 0.4, 'Europe': 0.9},
    'winter': {'Bulgaria': 0.7, 'Balkans': 0.8, 'Europe': 0.9}
}

destination = 'Bulgaria'
accommodation = 'Camp'
amount = 0

if 100 < budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'
if season == 'winter' or destination == 'Europe':
    accommodation = 'Hotel'

amount = plan.get(season).get(destination) * budget
result = f'Somewhere in {destination}\n{accommodation} - {amount:.2f}'
print(result)
