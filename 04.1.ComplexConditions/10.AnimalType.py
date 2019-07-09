animal = input()
animals = {
    'mammal': ['dog'],
    'reptile': ['crocodile', 'tortoise', 'snake']
}
not_found = True
for vertebrate_class, value in animals.items():
    for item in value:
        if item == animal:
            print(vertebrate_class)
            not_found = False

if not_found:
    print('unknown')
