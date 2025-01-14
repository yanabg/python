# read input
n = int(input())

# flag to check if comb.was found:
found = False

# iterate over all possible values of a,b,c,d:
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                # calc. total sum and total product:
                total_sum = a + b + c + d
                total_product = a * b * c * d
                # check if sum = product and n ends in 5
                if total_sum == total_product and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    found = True
                    break

                # Check if product divided by sum equals 3 and n is divisible by 3
                if total_product // total_sum == 3 and n % 3 == 0 and total_product != 0:
                    print(f'{d}{c}{b}{a}')
                    if found:
                        break

            # If a valid combination is found => break the loop
            if found:
                break
        if found:
            break
    if found:
        break
# if no valid comb. is found:
if not found:
    print("Nothing was found")
