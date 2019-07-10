exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

status = 'On time'
summary = ''
exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
difference_in_minutes = exam_time - arrival_time

if 0 < difference_in_minutes <= 30:
    summary = f'{difference_in_minutes} minutes before the start'
elif difference_in_minutes < 0:
    status = 'Late'
    difference_in_minutes = arrival_time - exam_time
    if difference_in_minutes < 60:
        summary = f'{abs(difference_in_minutes)} minutes'
    else:
        summary = f'{abs(int(difference_in_minutes/60))}:{difference_in_minutes%60:02} hours'
    summary += ' after the start'
elif difference_in_minutes > 30:
    status = 'Early'
    if difference_in_minutes < 60:
        summary = f'{difference_in_minutes} minutes'
    else:
        summary = f'{abs(int(difference_in_minutes/60))}:{difference_in_minutes%60:02} hours'
    summary += ' before the start'

print(status)
print(summary)
