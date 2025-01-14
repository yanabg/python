chrysanthemums = int(input())
rose = int(input())
tulip = int(input())
season = input()
is_holiday = input()

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00
    price_rose = 4.10
    price_tulip = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_rose = 4.50
    price_tulip = 4.15

total_price = (chrysanthemums * price_chrysanthemums) +\
    (rose * price_rose) +\
    (tulip * price_tulip)


if is_holiday == "Y":
    total_price *= 1.15

if tulip > 7 and season == "Spring":
    total_price *= 0.95
if rose >= 10 and season == "Winter":
    total_price *= 0.90
if chrysanthemums + rose + tulip > 20:
    total_price *= 0.80

total_price += 2

print(f'{total_price:.2f}')
