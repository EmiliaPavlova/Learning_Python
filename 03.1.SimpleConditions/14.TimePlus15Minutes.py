hours = int(input())
minutes = int(input())
addition = 15

minutes += addition
if minutes > 59:
    minutes -= 60
    hours += 1
    if hours > 23:
        hours -= 24

print('{0}:{1:02}'.format(hours, abs(minutes)))
