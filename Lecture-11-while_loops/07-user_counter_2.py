user_counter = 0

while True:
    user_counter += 1
    username = input()

    if user_counter == 3:
        break

    print(f'Hello, {username}!')