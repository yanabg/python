strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = 0.50 * strawberries_price
oranges_price = 0.60 * raspberries_price
bananas_price = 0.20 * raspberries_price

# print(f'rasp_price is: {raspberries_price}')
# print(f'orange_price is: {oranges_price}')
# print(f'banana price is: {bananas_price}')

amount_raspberries = raspberries_kg * raspberries_price
amount_oranges = oranges_kg * oranges_price
amount_bananas = bananas_kg * bananas_price
amount_strawberries = strawberries_kg * strawberries_price

# print(f'Rasp_amount is: {raspberries_kg} * {raspberries_price} = {amount_raspberries}')
# print(f'Oranges_amount is: {oranges_kg} * {oranges_price} = {amount_oranges}')
# print(f'Oranges_amount is: {bananas_kg} * {bananas_price} = {amount_bananas}')
# print(f'Oranges_amount is: {strawberries_kg} * {strawberries_price} = {amount_strawberries}')

total_amount = amount_raspberries + amount_oranges + amount_bananas + amount_strawberries

# print(f'Total amount: {amount_raspberries} + {amount_oranges} + {amount_bananas} + {amount_strawberries} = {total_amount:.2f}')
print(f'{total_amount:.2f}')