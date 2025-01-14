egg_size = input()
egg_color = input()
batches_count = int(input())

price_per_egg = 0

if egg_size == "Large":
    if egg_color == "Red":
        price_per_egg = 16
    elif egg_color == "Green":
        price_per_egg = 12
    elif egg_color == "Yellow":
        price_per_egg = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price_per_egg = 13
    elif egg_color == "Green":
        price_per_egg = 9
    elif egg_color == "Yellow":
        price_per_egg = 7
elif egg_size == "Small":
    if egg_color == "Red":
        price_per_egg = 9
    elif egg_color == "Green":
        price_per_egg = 8
    elif egg_color == "Yellow":
        price_per_egg = 5

price = batches_count * price_per_egg
production_costs = price * 0.35
final_cost = price - production_costs

print(f'{final_cost:.2f} leva.')