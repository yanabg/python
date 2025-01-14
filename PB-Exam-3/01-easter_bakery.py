flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_crusts = int(input())
yeast_packet = int(input())

sugar_price = flour_price * 0.75
egg_crust_price = flour_price * 1.10
yeast_packet_price = sugar_price * 0.20

total_cost = flour_kg * flour_price +\
    sugar_kg * sugar_price +\
    egg_crusts * egg_crust_price +\
    yeast_packet * yeast_packet_price

print(f'{total_cost:.2f}')