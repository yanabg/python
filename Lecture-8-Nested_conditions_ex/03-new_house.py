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
number_flowers = int(input())
budget = int(input())

discounted_price_rose = PRICE_ROSE * (1 - DISCOUNT_ROSE)
discounted_price_dalia = PRICE_DALIA * (1 - DISCOUNT_DALIA)
discounted_price_tulip = PRICE_TULIP * (1 - DISCOUNT_TULIP)
increased_price_narcis = PRICE_NARCIS * (1 + INCREASE_NARCIS)
increased_price_gladiola = PRICE_GLADIOLA * (1 + INCREASE_GLADIOLA)

total_cost = 0
difference = budget - total_cost

if flowers_type == "Roses":
    if number_flowers > 80:
        total_cost = number_flowers * discounted_price_rose
    else:
        total_cost = number_flowers * PRICE_ROSE
 #       print(f"total cost is: {total_cost:.2f} ")
elif flowers_type == "Dahlias":
    if number_flowers > 90:
        total_cost = number_flowers * discounted_price_dalia
    else:
        total_cost = number_flowers * PRICE_DALIA
 #       print(f"total cost is: {total_cost:.2f} ")
elif flowers_type == "Tulips":
    if number_flowers > 80:
        total_cost = number_flowers * discounted_price_tulip
    else:
        total_cost = number_flowers * PRICE_TULIP
 #       print(f"total cost is: {total_cost:.2f} ")
elif flowers_type == "Narcissus":
    if number_flowers < 120:
        total_cost = number_flowers * increased_price_narcis
    else:
        total_cost = number_flowers * PRICE_NARCIS
#        print(f"total cost is: {total_cost:.2f} ")
elif flowers_type == "Gladiolus":
    if number_flowers < 80:
        total_cost = number_flowers * increased_price_gladiola
    else:
        total_cost = number_flowers * PRICE_GLADIOLA
#        print(f"total cost is: {total_cost:.2f} ")

if total_cost <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {flowers_type} and {budget - total_cost:.2f} leva left.")
elif total_cost >= budget:
    difference = abs(budget - total_cost)
    print(f"Not enough money, you need {difference:.2f} leva more.")