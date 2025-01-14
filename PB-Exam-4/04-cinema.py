TICKET_PRICE = 5

capacity = int(input())
remaining_seats = capacity
income = 0

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {remaining_seats} seats left in the cinema.")
        print(f"Cinema income - {income} lv.")
        break

    people_entering = int(command)
    if people_entering > remaining_seats:
        print(f'The cinema is full.')
        print(f"Cinema income - {income} lv.")
        break

    # calc income for the current group
    current_income = people_entering * TICKET_PRICE

    if people_entering % 3 == 0:
        current_income -= 5

    income += current_income
    remaining_seats -= people_entering