fruit = input()
set_size = input()
num_sets_ordered = int(input())

if fruit == "Watermelon":
    if set_size == "small":
        count = 2
        price_per_item = 56
    if set_size == "big":
        count = 5
        price_per_item = 28.70
elif fruit == "Mango":
    if set_size == "small":
        count = 2
        price_per_item = 36.66
    if set_size == "big":
        count = 5
        price_per_item = 19.60
elif fruit == "Pineapple":
    if set_size == "small":
        count = 2
        price_per_item = 42.10
    if set_size == "big":
        count = 5
        price_per_item = 24.80
elif fruit == "Raspberry":
    if set_size == "small":
        count = 2
        price_per_item = 20
    if set_size == "big":
        count = 5
        price_per_item = 15.20

total_amount = num_sets_ordered * count * price_per_item
if 400 <= total_amount <= 1000:
    total_amount *= 0.85
elif total_amount > 1000:
    total_amount *= 0.50

print(f'{total_amount:.2f} lv.')