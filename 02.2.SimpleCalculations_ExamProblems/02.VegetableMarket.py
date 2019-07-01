vegetables_lev = float(input())
fruits_lev = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())
fixing_eur_lev = 1.94

incomes_vegetables = vegetables_lev * vegetables_kg
incomes_fruits = fruits_lev * fruits_kg
incomes_total = (incomes_vegetables + incomes_fruits) / fixing_eur_lev
print(incomes_total)
