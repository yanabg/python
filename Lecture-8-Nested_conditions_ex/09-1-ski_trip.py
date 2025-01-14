SINGLE_ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

nights = int(input()) - 1
room_type = input()
rating = input()

if room_type == "room for one person":
    price = SINGLE_ROOM

elif room_type == "apartment":
    price = APARTMENT

    if nights < 10:
        price *= 0.70
    elif nights <= 15:
        price *= 0.65
    else:
        price *= 0.50

elif room_type == "president apartment":
    price = PRESIDENT_APARTMENT

    if nights < 10:
        price *= 0.90
    elif nights <= 15:
        price *= 0.85
    else:
        price *= 0.80
if rating == "positive":
    price *= 1.25

elif rating == "negative":
    price *= 0.90

total_price = price * nights
print(f"{total_price:.2f}")
