number = int(input())
counter = 0

for row in range(1, number + 1):
    for cols in range(1, row + 1):
        counter += 1

        print(counter, end=" ")

        if counter == number:
            exit()

    print()