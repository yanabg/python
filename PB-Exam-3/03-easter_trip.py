destination = input()
dates = input()
nights = int(input())

cost_per_night = 0

if destination == "France":
    if dates == "21-23":
        cost_per_night = 30
    elif dates == "24-27":
        cost_per_night = 35
    elif dates == "28-31":
        cost_per_night = 40
elif destination == "Italy":
    if dates == "21-23":
        cost_per_night = 28
    elif dates == "24-27":
        cost_per_night = 32
    elif dates == "28-31":
        cost_per_night = 39
elif destination == "Germany":
    if dates == "21-23":
        cost_per_night = 32
    elif dates == "24-27":
        cost_per_night = 37
    elif dates == "28-31":
        cost_per_night = 43

total_cost = cost_per_night * nights
print(f'Easter trip to {destination} : {total_cost:.2f} leva.')