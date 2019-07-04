holidays = int(input())
days_in_year = 365
work_days = days_in_year - holidays
playing_time_workday = 63
playing_time_holiday = 127
playing_standard_yearly = 30000

total_playing_time = work_days * playing_time_workday + holidays * playing_time_holiday
difference = abs(total_playing_time - playing_standard_yearly)
difference_in_hours = int(difference / 60)
difference_in_minutes = difference - difference_in_hours * 60

print(f'Tom will run away\n{difference_in_hours} hours and {difference_in_minutes} minutes more for play'
      if total_playing_time > playing_standard_yearly
      else f'Tom sleeps well\n{difference_in_hours} hours and {difference_in_minutes} minutes less for play')
