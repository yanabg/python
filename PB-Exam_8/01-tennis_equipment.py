from math import floor, ceil
rocket_price = float(input())
rocket_count = int(input())
pair_trainers = int(input())

rocket_cost = rocket_count * rocket_price
# print(f'rocket cost os: {rocket_cost}')

trainers_price = rocket_price / 6
trainers_cost = trainers_price * pair_trainers
# print(f'trainers_cost is: {trainers_cost}')

other_equipment_cost = 0.2 * (rocket_cost + trainers_cost)
# print(f'other equipment cost: {other_equipment_cost}')

total_cost = rocket_cost + trainers_cost + other_equipment_cost

djokovic_payment = total_cost / 8
sponsors_payment = total_cost * 7 / 8

print(f'Price to be paid by Djokovic {floor(djokovic_payment)}')
print(f'Price to be paid by sponsors {ceil(sponsors_payment)}')


