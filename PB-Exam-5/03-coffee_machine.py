drink = input()
sugar = input()
drink_num = int(input())

item_price = 0
discount_rate = 0

if drink == "Espresso":
    if sugar == "Without":
        item_price = 0.90
    elif sugar == "Normal":
        item_price = 1.00
    elif sugar == "Extra":
        item_price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        item_price = 1.00
    elif sugar == "Normal":
        item_price = 1.20
    elif sugar == "Extra":
        item_price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        item_price = 0.50
    elif sugar == "Normal":
        item_price = 0.60
    elif sugar == "Extra":
        item_price = 0.70
# discounts
if sugar == "Without":
    item_price *= 0.65
if drink == "Espresso" and drink_num >= 5:
    item_price *= 0.75

total_price = drink_num * item_price

if total_price > 15:
    total_price *= 0.80

print(f'You bought {drink_num} cups of {drink} for {total_price:.2f} lv.')

