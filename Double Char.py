command = input()
while command != "End":
    string = command
    if string == "SoftUni":
        command = input()
        continue
    for i in range (0, len(string)):
        char = string[i]
        for j in range(0, 2):
            print(char, end='')
    print()
    command = input()
