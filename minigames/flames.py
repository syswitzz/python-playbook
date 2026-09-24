name1 = list(input("Enter the first name: ").replace(' ', '').lower())
name2 = list(input("Enter the second name: ").replace(' ', '').lower())

non_matching_letters = [char for char in name1 if char not in name2] + [char for char in name2 if char not in name1]
count = len(non_matching_letters)

result = ["friends", 'love', 'affection', 'marriage', 'enemy', 'siblings']

while len(result) > 1:
    index = (count%len(result)) - 1

    if index >= 0:
        result = result[index+1:] + result[:index]
    else:
        result = result[:len(result)-1]

print(f'\n{''.join(name1).capitalize()} + {''.join(name2).capitalize()} are made for {result[0].capitalize()}')

