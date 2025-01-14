annual_fee = int(input())

sneakers_price = 0.60 * annual_fee
kit = 0.80 * sneakers_price
ball = kit / 4
accessories = ball /5

# print(sneakers_price)
# print(kit)
# print(ball)
# print(accessories)

total_price = annual_fee + sneakers_price +\
        kit + accessories + ball
print(f'{total_price:.2f}')