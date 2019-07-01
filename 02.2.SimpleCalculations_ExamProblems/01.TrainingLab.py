length = float(input()) * 100
width = float(input()) * 100

work_place_length = 120
work_place_width = 70
corridor = 100
entrance_door = 1
desk = 2

rows = int(length / work_place_length)
available_width = width - corridor
columns = int(available_width / work_place_width)
number_work_places = rows * columns - entrance_door - desk

print(number_work_places)
