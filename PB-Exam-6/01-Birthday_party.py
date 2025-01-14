hall_price = float(input())

cake_price = 0.20 * hall_price
drinks = cake_price * 0.55
animation = hall_price / 3

costs = cake_price +\
    animation +\
    hall_price +\
    drinks

print(f'{costs:.2f}')
# print(f'{cake_price}')
# print(f'{drinks}')
# print(f'{animation}')