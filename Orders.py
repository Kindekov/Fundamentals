number_of_orders = int(input())
total_price = 0
for i in range (number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules = int(input())
    price = capsule_price * days * capsules
    if capsule_price > 100 or capsule_price < 0.01 or days not in range(1, 32) or capsules not in range(1, 2001):
        number_of_orders += 1
        continue
    else:
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
print(f"Total: ${total_price:.2f}")
