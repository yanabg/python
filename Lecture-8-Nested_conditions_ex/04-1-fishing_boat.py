PRICE_BOAT_SPRING = 3000
PRICE_BOAT_SUMMER_AUTUMN = 4200
PRICE_BOAT_WINTER = 2600

DISCOUNT_UP_TO_SIX = 0.10
DISCOUNT_SEVEN_TO_ELEVEN = 0.15
DISCOUNT_MORE_THAN_TWELVE = 0.25

DISCOUNT_EVEN = 0.05

budget = int(input())
season = input()
count_people = int(input())

total_price = 0

if season == "Spring":
    total_price = PRICE_BOAT_SPRING
elif season == "Winter":
    total_price = PRICE_BOAT_WINTER
else:
    total_price = PRICE_BOAT_SUMMER_AUTUMN

if count_people <= 6:
    total_price *= (1 - DISCOUNT_UP_TO_SIX)
elif 7 <= count_people <= 11:
    total_price *= (1 - DISCOUNT_SEVEN_TO_ELEVEN)
else:
    total_price *= (1 - DISCOUNT_MORE_THAN_TWELVE)

if season != "Autumn" and count_people % 2 == 0:
    total_price *= (1 - DISCOUNT_EVEN)

if total_price <= budget:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")
