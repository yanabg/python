hundreds_limit = int(input())
tens_limit = int(input())
ones_limit = int(input())

for hundreds in range(2, hundreds_limit + 1, 2):
    for tens in range(2, tens_limit + 1):
            if tens == 2 or tens == 3 or tens == 5 or tens == 7:
                for ones in range(2, ones_limit + 1, 2):
                    print(f'{hundreds} {tens} {ones}')
