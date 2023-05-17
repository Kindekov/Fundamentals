command = input()
house = ''
while command != "Welcome!":
    name = command
    if name == "Voldemort":
        print('You must not speak of that name!')
        break
    elif len(name) < 5:
        house = 'Gryffindor'
    elif len(name) == 5:
        house = 'Slytherin'
    elif len(name) == 6:
        house = 'Ravenclaw'
    else:
        house = 'Hufflepuff'
    print(f'{name} goes to {house}.')
    command = input()
else:
    print("Welcome to Hogwarts.")
