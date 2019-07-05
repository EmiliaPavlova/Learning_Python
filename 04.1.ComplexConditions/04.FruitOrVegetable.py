entry = input()
fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']

if entry in fruits:
    print('fruit')
elif entry in vegetables:
    print('vegetable')
else:
    print('unknown')
