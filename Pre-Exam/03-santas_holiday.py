PRICE_ROOM_FOR_ONE_PER_NIGHT = 18
PRICE_APARTMENT_PER_NIGHT = 25
PRICE_PRESIDENT_AP_PER_NIGHT = 35

stay_days = int(input())
room_type = input()
rating = input()

price_per_night = 0

if room_type == "room for one person":
    price_per_night = PRICE_ROOM_FOR_ONE_PER_NIGHT
elif room_type == "apartment":
    if stay_days < 10:
        price_per_night = 0.70 * PRICE_APARTMENT_PER_NIGHT
    elif stay_days <= 15:
        price_per_night = 0.65 * PRICE_APARTMENT_PER_NIGHT
    elif stay_days > 15:
        price_per_night = 0.50 * PRICE_APARTMENT_PER_NIGHT
elif room_type == "president apartment":
    if stay_days < 10:
        price_per_night = 0.90 * PRICE_PRESIDENT_AP_PER_NIGHT
    elif stay_days <= 15:
        price_per_night = 0.85 * PRICE_PRESIDENT_AP_PER_NIGHT
    elif stay_days > 15:
        price_per_night = 0.80 * PRICE_PRESIDENT_AP_PER_NIGHT

total_price = (stay_days - 1) * price_per_night
if rating == 'positive':
    total_price *= 1.25
elif rating == 'negative':
    total_price *= 0.90

print(f'{total_price:.2f}')