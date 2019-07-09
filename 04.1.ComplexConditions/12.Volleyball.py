year = input().lower()
holidays = int(input())
weekends_traveling = int(input())
weekends = 48
weekends_sofia = (weekends - weekends_traveling) * 3/4
days_to_play = weekends_sofia + weekends_traveling + 2/3 * holidays

# check for leap year
if year == 'leap':
    days_to_play += (days_to_play * 15/100)

print(int(days_to_play))
