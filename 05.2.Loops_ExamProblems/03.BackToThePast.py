heritage = float(input())
year_to_live = int(input())

age = 18
starting_year = 1800
even_year_amount = 12000

for currant_age in range(starting_year, year_to_live + 1):
    if currant_age % 2 == 0:
        heritage -= even_year_amount
    else:
        heritage -= (even_year_amount + 50 * age)
    age += 1

print(f'Yes! He will live a carefree life and will have {heritage:.2f} dollars left.'
      if heritage >= 0
      else f'He will need {abs(heritage):.2f} dollars to survive.')
