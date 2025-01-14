command = input()
meters_count = 5364
days_counter = 1

while command != "END":
    meters = int(input())

    if command == "Yes":
        days_counter += 1
        if days_counter > 5:
            print("Failed!")
            print(meters_count)
            break
        meters_count += meters
    else:
        meters_count += meters

    if meters_count >= 8848:
        print(f"Goal reached for {days_counter} days!")
        break

    command = input()

if command == "End":
    if meters_count >= 8848:
        print(f"Goal reached for {days_counter} days!")
    else:
        print("Failed!")
        print(meters_count)