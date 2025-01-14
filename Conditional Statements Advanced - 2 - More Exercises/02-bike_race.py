juniors = int(input())
seniors = int(input())
trace_type = input()

total_participants = juniors + seniors

if trace_type == "trail":
    juniors_price = 5.50
    seniors_price = 7.00
elif trace_type == "cross-country":
    juniors_price = 8.00
    seniors_price = 9.50
elif trace_type == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif trace_type == "road":
    juniors_price = 20.00
    seniors_price = 21.50

total_price = (juniors * juniors_price) + (seniors * seniors_price)

if trace_type == "cross-country" and total_participants >= 50:
    total_price *= 0.75

total_price *= 0.95

print(f'{total_price:.2f}')