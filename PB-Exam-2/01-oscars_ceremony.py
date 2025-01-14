hall_rent = int(input())

statue_price = 0.70 * hall_rent
catering_price = 0.85 * statue_price
sound_price = catering_price / 2

total_cost = hall_rent +\
            sound_price +\
            catering_price +\
            statue_price
# print(statue_price)
# print(catering_price)
# print(sound_price)
print(f'{total_cost:.2f}')