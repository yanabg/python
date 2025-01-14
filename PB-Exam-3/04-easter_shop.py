initial_eggs = int(input())
total_sold = 0

current_eggs = initial_eggs

while True:
    command = input()

    if command == "Close":
        print("Store is closed!")
        print(f"{total_sold} eggs sold.")
        break

    quantity = int(input())

    if command == "Buy":
        if quantity > current_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {current_eggs}.")
            break
        else:
            current_eggs -= quantity
            total_sold += quantity
    elif command == "Fill":
        current_eggs += quantity

