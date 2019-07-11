from sys import maxsize

n = int(input())
biggest_number = -maxsize
for i in range(0, n):
    number = int(input())
    if biggest_number < number:
        biggest_number = number
print(biggest_number)
