budget = float(input())

while True:
    command = input()

    if command == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break

    actor_name = command

    if len(actor_name) > 15:
        actor_salary = budget * 0.20
    else:
        actor_salary = float(input())

    budget -= actor_salary

    if budget < 0:
        print(f'We need {-budget:.2f} leva for our actors.')
        break