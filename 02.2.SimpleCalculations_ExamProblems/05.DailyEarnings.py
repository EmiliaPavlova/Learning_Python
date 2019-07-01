working_days_month = int(input())
earned_money_day = float(input())
rate_dollar_lev = float(input())

bonus_index = 2.5
taxes = 25 / 100
days = 365
monthly_salary = working_days_month * earned_money_day
yearly_income = monthly_salary * 12 + monthly_salary * bonus_index
yearly_income -= yearly_income * taxes
yearly_income *= rate_dollar_lev
average_daily_income = yearly_income / days
print('%.2f' % average_daily_income)
