budget = float(input())
flour_price = float(input())
egg_price = 0.75 * flour_price
milk_price_litre = 1.25 * flour_price
cooking_loaf_cost = egg_price + flour_price + (milk_price_litre * 0.25)
loaf_count = 0
colored_eggs_received = 0
while budget >= cooking_loaf_cost:
    loaf_count += 1
    colored_eggs_received += 3
    if loaf_count % 3 == 0:
        colored_eggs_received -= loaf_count - 2
    budget -= cooking_loaf_cost
print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs_received} eggs and {budget:.2f}BGN left.")
