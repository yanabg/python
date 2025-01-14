age = int(input())
price_washing_m = float(input())
toy_price = int(input())
toys_count = 0
savings = 0
money_increment = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        savings += money_increment - 1
        money_increment += 10
    else:
        toys_count += 1

total_savings = savings + toys_count * toy_price

if total_savings >= price_washing_m:
    print(f'Yes! {total_savings - price_washing_m:.2f}')
else:
    print(f'No! {price_washing_m - total_savings:.2f}')

