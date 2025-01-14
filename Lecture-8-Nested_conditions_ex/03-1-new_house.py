PRICE_ROSE = 5
PRICE_DALIA = 3.80
PRICE_TULIP = 2.80
PRICE_NARCIS = 3
PRICE_GLADIOLA = 2.50

DISCOUNT_ROSE = 0.10
DISCOUNT_DALIA = 0.15
DISCOUNT_TULIP = 0.15
INCREASE_NARCIS = 0.15
INCREASE_GLADIOLA = 0.20

flowers_type = input()
count_flowers = int(input())
budget = int(input())

total_price = 0

if flowers_type == "Roses":
    total_price = count_flowers * PRICE_ROSE

    if count_flowers > 80:
        total_price *= 0.90 # 10% discount

elif flowers_type == "Dahlias":
    total_price = count_flowers * PRICE_DALIA

    if count_flowers > 90:
        total_price *= 0.85 # 15% discount

elif flowers_type == "Tulips":
    total_price = count_flowers * PRICE_TULIP

    if count_flowers > 80:
        total_price *= 0.85 # 15% discount

elif flowers_type == "Narcissus":
    total_price = count_flowers * PRICE_NARCIS

    if count_flowers < 120:
        total_price *= 1.15 # 15% Uplift

elif flowers_type == "Gladiolus":
    total_price = count_flowers * PRICE_GLADIOLA

    if count_flowers < 80:
        total_price *= 1.20 # 20% Uplift

if total_price <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {flowers_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
