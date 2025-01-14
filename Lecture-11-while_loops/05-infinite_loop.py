a = 10

while a > 0:
    print(a)

    # if no step for changing a => infinite loop
    #a -= 1

b = 1

while b < 6:
    print(b)
    # b += 1

while True:
    print('Infinite loop')

while True:
    username = input()

    # exit loop:
    if username == 'admin':
        break
    print(f'Hello, {username}!')

while True:
    username = input()

    if user_counter == 3:
        break

        user_counter += 1
        print(f'Hello, {username}!')