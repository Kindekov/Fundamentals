number = int(input())
for i in range(0, number):
    text = input()
    for j in range(0, len(text)):
        letter = text[j]
        if letter == ',' or letter == '.' or letter == '_':
            print(f'{text} is not pure!')
            break
    else:
        print(f'{text} is pure.')
