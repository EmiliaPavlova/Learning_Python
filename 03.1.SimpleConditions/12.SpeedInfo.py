speed = float(input())
slow = 10
average = 50
fast = 150
if speed <= slow:
    print('slow')
elif speed <= average:
    print('average')
elif speed <= 150:
    print('fast')
elif speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
