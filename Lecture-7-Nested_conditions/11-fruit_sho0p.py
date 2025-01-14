weekday_prices = {
    "banana": 2.50,
    "apple": 1.2,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

fruit = input()
day = input().lower()
quantity = float(input())

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    prices = weekday_prices
elif day in ["saturday", "sunday"]:
    prices = weekend_prices
else:
    prices = None

if prices is None:
    print("error")
elif fruit not in prices:
    print("error")
else:
    total_price = prices[fruit] * quantity
    print(f"{total_price:.2f}")



















