number = int(input())
highest_value = list(str(number))
highest_value.sort(reverse=True)
for i in highest_value:
    print(i, end="")
