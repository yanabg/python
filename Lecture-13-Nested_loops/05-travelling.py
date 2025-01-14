# destination = input()
# budget = float(input())

while True:
    destination = input()

    if destination == "End":
        break

    min_budget = float(input())
    saved_amount = 0

    while saved_amount < min_budget:
        amount = float(input())
        saved_amount += amount
    print(f'Going to {destination}!')