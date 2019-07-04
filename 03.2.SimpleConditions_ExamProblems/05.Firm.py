import math

required_hours = int(input())
given_days = int(input())
employees = int(input())
occupied_days = 0.1 * given_days
available_days = given_days - occupied_days
working_time = 10

total_hours = available_days * employees * working_time
net_hours = abs(math.floor(required_hours - total_hours))

print(f'Yes!{net_hours} hours left.' if required_hours <= total_hours else f'Not enough time!{net_hours} hours needed.')
