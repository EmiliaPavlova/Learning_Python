from sys import maxsize

n = int(input())
smallest_number = maxsize
for i in range(0, n):
    number = int(input())
    if smallest_number > number:
        smallest_number = number
print(smallest_number)
