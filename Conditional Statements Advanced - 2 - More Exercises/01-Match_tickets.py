VIP_TICKET = 499.99
NORMAL_TICKET = 249.99

budget = float(input())
category = input()
people_count = int(input())

transport_cost = 0
tickets_cost = 0

if 1 <= people_count <= 4:
    transport_cost = budget * 0.75
elif 5 <= people_count <= 9:
    transport_cost = budget * 0.60
elif 10 <= people_count <= 24:
    transport_cost = budget * 0.50
elif 25 <= people_count <= 49:
    transport_cost = budget * 0.40
else:
    transport_cost = budget * 0.25

if category == "VIP":
    tickets_cost = people_count * VIP_TICKET
elif category == "Normal":
    tickets_cost = people_count * NORMAL_TICKET

remaining_amount = budget - transport_cost

if remaining_amount >= tickets_cost:
    print(f'Yes! You have {remaining_amount - tickets_cost:.2f} leva left.')
elif remaining_amount < tickets_cost:
    print(f"Not enough money! You need {abs(remaining_amount - tickets_cost):.2f} leva.")