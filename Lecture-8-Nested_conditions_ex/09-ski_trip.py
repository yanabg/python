SINGLE_ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

nights = int(input()) - 1
room_type = input()
rating = input()

price = 0

if nights < 10:
    if room_type == "room for one person":
        price = SINGLE_ROOM
    elif room_type == "apartment":
        price *= APARTMENT * 0.7
    elif room_type == "president apartment":
        price = PRESIDENT_APARTMENT * 0.9
elif 10 >= nights or nights <= 15:
    if room_type == "room for one person":
        price = SINGLE_ROOM
    elif room_type == "apartment":
        price = APARTMENT * 0.65
        print(f'the price is {price:.2f}')
    elif room_type == "president apartment":
        price = PRESIDENT_APARTMENT * 0.85
elif nights > 15:
    if room_type == "room for one person":
        price = SINGLE_ROOM
    elif room_type == "apartment":
        price *= APARTMENT * 0.5
    elif room_type == "president apartment":
        price = PRESIDENT_APARTMENT * 0.8
        print(f"president apartment price is: {price:.2f}")

if rating == "positive":
    print(f'the price before +25% is {price:.2f}')
    price *= 1.25
    print(f'the price after +25% is {price:.2f}')
elif rating == "negative":
    print(f'the price before -10% is {price:.2f}')
    price *= 0.90
    print(f'the price after -10% is {price:.2f}')

total_price = price * nights
print(room_type)
print(f"{price}")
print(f"{nights}")
print(f"{total_price:.2f}")
