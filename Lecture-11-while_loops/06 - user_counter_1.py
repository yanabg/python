user_counter = 0

while True:
    username = input()

    if user_counter == 3:
        break

    user_counter += 1
    print(f'Hello, {username}!')