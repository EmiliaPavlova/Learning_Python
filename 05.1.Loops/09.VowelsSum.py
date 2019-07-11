text = input()
vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
vowels_sum = 0
for i in text:
    vowels_sum += vowels.get(i, 0)

print(vowels_sum)
