from math import ceil

guests = int(input())
budget = int(input())

trumpet_price = 4
egg_price = 0.45

needed_trumpets = ceil(guests / 3)
needed_eggs = guests * 2

trumpets_price = needed_trumpets * trumpet_price
eggs_price = needed_eggs * egg_price

total_price = trumpets_price + eggs_price

if total_price <= budget:
    print(f'Lyubo bought {ceil(needed_trumpets)} Easter bread and {needed_eggs} eggs.')
    print(f'He has {budget - total_price:.2f} lv. left.')
elif budget < total_price:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {total_price - budget:.2f} lv. more.')