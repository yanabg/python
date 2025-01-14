city = input()
packet_type = input()
vip_discount = input()
stay_days = int(input())

daily_price = 0
discount_rate = 0

if stay_days < 1:
    print('Days must be positive number!')
    exit()

if city == "Bansko" or city == "Borovets":
    if packet_type == "withEquipment":
        daily_price = 100
        if vip_discount == "yes":
            daily_price *= 0.90
    elif packet_type == "noEquipment":
        daily_price = 80
        if vip_discount == "yes":
            daily_price *= 0.95
    else:
        print("Invalid input!")
        exit()
elif city == "Varna" or city == "Burgas":
    if packet_type == "withBreakfast":
        daily_price = 130
        if vip_discount == "yes":
            daily_price *= 0.88
    elif packet_type == "noBreakfast":
        daily_price = 100
        if vip_discount == "yes":
            daily_price *= 0.93
    else:
        print("Invalid input!")
        exit()
else:
    print(f'Invalid input!')
    exit()

if stay_days > 7:
    stay_days -= 1
total_price = stay_days * daily_price

print(f'The price is {total_price:.2f}lv! Have a nice time!')

