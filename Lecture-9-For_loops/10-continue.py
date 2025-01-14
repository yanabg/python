for number in range(1, 11):
    if number % 2 != 0:
        continue # doesn't break the loop but returns at the beginning to iterate again
    print(number)