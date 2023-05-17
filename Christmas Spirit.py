qty_of_decorations = int(input())
days_until_Xmas = int(input())
ornament_set_price = 2
ornament_spirit_pts = 5
skirt_set_price = 5
skirt_spirit_pts = 3
garland_set_price = 3
garland_spirit_pts = 10
lights_set_price = 15
lights_spirit_pts = 17
shopping_cost = 0
spirit_pts = 0

for i in range(1, days_until_Xmas+1):
    if i % 11 == 0:
        qty_of_decorations += 2
    if i % 10 == 0:
        spirit_pts -= 20
        shopping_cost += lights_set_price + garland_set_price + skirt_set_price
        if i == days_until_Xmas:
            spirit_pts -= 30
    if i % 5 == 0:
        shopping_cost += lights_set_price * qty_of_decorations
        spirit_pts += lights_spirit_pts
    if i % 15 == 0:
        spirit_pts += 30
    if i % 3 == 0:
        shopping_cost += (skirt_set_price + garland_set_price) * qty_of_decorations
        spirit_pts += skirt_spirit_pts + garland_spirit_pts
    if i % 2 == 0:
        shopping_cost += ornament_set_price * qty_of_decorations
        spirit_pts += ornament_spirit_pts
print(f'Total cost: {shopping_cost}')
print(f'Total spirit: {spirit_pts}')
