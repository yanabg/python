film_name = input()
hall_type = input()
tickets_num = int(input())

ticket_price = 0

if film_name == "A Star Is Born":
    if hall_type == "normal":
        ticket_price = 7.50
    elif hall_type == "luxury":
        ticket_price = 10.50
    elif hall_type == "ultra luxury":
        ticket_price = 13.50

elif film_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        ticket_price = 7.35
    elif hall_type == "luxury":
        ticket_price = 94.5
    elif hall_type == "ultra luxury":
        ticket_price = 12.75

elif film_name == "Green Book":
    if hall_type == "normal":
        ticket_price = 8.15
    elif hall_type == "luxury":
        ticket_price = 10.25
    elif hall_type == "ultra luxury":
        ticket_price = 13.25

elif film_name == "The Favourite":
    if hall_type == "normal":
        ticket_price = 8.75
    elif hall_type == "luxury":
        ticket_price = 11.55
    elif hall_type == "ultra luxury":
        ticket_price = 13.95

total_income = tickets_num * ticket_price
print(f'{film_name} -> {total_income:.2f} lv.')