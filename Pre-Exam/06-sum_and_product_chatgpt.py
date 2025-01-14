# Read the input number n
n = int(input())

# Initialize a flag to check if a valid combination is found
found = False

# Iterate through all possible values of a, b, c, d
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                # Calculate the sum and product of the digits
                total_sum = a + b + c + d
                total_product = a * b * c * d

                # Check if the sum equals the product and n ends in 5
                if total_sum == total_product and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    found = True
                    break

                # Check if product divided by sum equals 3 and n is divisible by 3
                if total_product != 0 and total_product // total_sum == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    found = True
                    break

            # If a valid combination is found, break the loop
            if found:
                break
        if found:
            break
    if found:
        break

# If no valid combination was found, print "Nothing found"
if not found:
    print("Nothing found")
