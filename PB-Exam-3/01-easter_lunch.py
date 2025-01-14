TRUMPET_PRICE = 3.20
EGGS_PRICE = 4.35 # for crust of 12 eggs
COOKIES_PRICE = 5.40 # per kg.
PAINT = 0.15 # per egg

trumpets_count = int(input())
egg_crusts_count = int(input())
cookies_kg = int(input())

total_cost = trumpets_count * TRUMPET_PRICE +\
    egg_crusts_count * EGGS_PRICE +\
    cookies_kg * COOKIES_PRICE +\
    egg_crusts_count * 12 * PAINT
print(f'{total_cost:.2f}')