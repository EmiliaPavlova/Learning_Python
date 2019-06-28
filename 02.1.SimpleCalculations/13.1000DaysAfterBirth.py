from datetime import datetime, timedelta

birth_date = input('Enter birth date in format dd-MM-yyyy: ')
date = datetime.strptime(birth_date, '%d-%m-%Y')
end_date = date + timedelta(days=1000)
print_date = end_date.strftime('%d-%m-%Y')
print(f'The date in 1000 days: {print_date}')

