command = input()
coffees = 0
while command != "END":
    event = command
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffees += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffees += 2
    if coffees > 5:
        print('You need extra sleep')
        break
    command = input()
else:
    print(coffees)
