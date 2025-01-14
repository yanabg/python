annual_fee = int(input())

shoes_price = 0.6 * annual_fee
# print(f"shoes price is {shoes_price}")

clothes_price = 0.8 * shoes_price
# print(f"clothes proce is: {clothes_price}")

ball_price = 0.25 * clothes_price
# print(f"ball price is: {ball_price}")

accessories_price = 0.20 * ball_price
# print(f"accessories price is: {accessories_price}")

total_cost = annual_fee + shoes_price + clothes_price + ball_price + accessories_price

print(total_cost)