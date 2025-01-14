# starting_conditions:
current_height_counter = 5364
climbing_days_counter = 1
max_days = 5
summit_height = 8848

while True:
    command = input()
    if command == "END": # can be "Yes", "No" or "END"
        break
    meters_climbed = int(input()) # read input for climbed meters
    if command == "Yes":
        climbing_days_counter += 1
        if climbing_days_counter > max_days:
            break
    current_height_counter += meters_climbed

    if current_height_counter >= summit_height:
        print(f'Goal reached for {climbing_days_counter} days!')
        break

if current_height_counter < summit_height:
    print("Failed!")
    print(f'{current_height_counter}')