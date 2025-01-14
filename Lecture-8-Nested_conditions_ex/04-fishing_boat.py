PRICE_BOAT_SPRING = 3000
PRICE_BOAT_SUMMER_AUTUMN = 4200
PRICE_BOAT_WINTER = 2600

budget = int(input())
season = input()
group_count = int(input())

DISCOUNT_UPTO_SIX = 0.10
DISCOUNT_SEVEN_TO_ELEVEN = 0.15
DISCOUNT_MORE_THAN_TWELVE = 0.25

DISCOUNT_EVEN = 0.05

price = 0

if season == "Summer" or season == "Autumn":
    if group_count <= 6:
        if group_count % 2 == 0 and season != "Autumn":
            price_h = PRICE_BOAT_SUMMER_AUTUMN * 0.90
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SUMMER_AUTUMN * 0.9
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif 7 <= group_count <= 11:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_SUMMER_AUTUMN * 0.85
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SUMMER_AUTUMN * 0.85
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif group_count >= 12:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_SUMMER_AUTUMN * 0.75
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SUMMER_AUTUMN * 0.75
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")

elif season == "Spring":
    if group_count <= 6:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_SPRING * 0.9
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SPRING * 0.9
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif 7 <= group_count <= 11:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_SPRING * 0.85
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SPRING * 0.85
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif group_count >= 12:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_SPRING * 0.75
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_SPRING * 0.75
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
elif season == "Winter":
    if group_count <= 6:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_WINTER * 0.90
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_WINTER * 0.9
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif 7 <= group_count <= 11:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_WINTER * 0.85
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_WINTER * 0.85
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
    elif group_count >= 12:
        if group_count % 2 == 0:
            price_h = PRICE_BOAT_WINTER * 0.75
            price = price_h * 0.95
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")
        else:
            price = PRICE_BOAT_WINTER * 0.75
            remaining_money = budget - price
            # print(f"price is: {price}")
            # print(f"remaining amount: {remaining_money:.2f}")


remaining_money = budget - price

if remaining_money >= 0:
    print(f"Yes! You have {remaining_money:.2f} leva left.")
elif remaining_money < 0:
    print(f"Not enough money! You need {abs(remaining_money):.2f} leva.")
else:
    print("error")
    exit()
