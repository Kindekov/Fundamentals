divisor = int(input())
boundary = int(input())
number = boundary
while number > divisor:
    if number % divisor == 0:
        print(number)
        break
    else:
        number -= 1
