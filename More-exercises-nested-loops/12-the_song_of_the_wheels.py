number = int(input())

# set counters
count = 0
password = ""
# generate all possible values for a, b, c and d in the range 1-9:
for a in range(1, 10): # to loop until 9 is reached (our range is 1-9)
    for b in range(1, 10):
        if a >= b: # condition a < b
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d: # condition is c > d
                    continue

                # calculate the control value"
                control_value = a * b + c * d
                if control_value == number:
                    count += 1
                    combination = f"{a}{b}{c}{d}"
                    print(combination, end=" ")

                    # If this is the 4th valid combination, store it as the password
                    if count == 4:
                        password = combination
# print new line for better output formatting:
print()

# print password if the 4th combination exists:
if password:
    print(f'Password: {password}')
else:
    print("No!")


# Explanation:
# Input Reading: We read the integer 𝑀
# M from the input, which represents the control value.
# Combination Generation: We use nested loops to generate all possible values of
# a, b, c, and d within the range [1, 9].
# Condition Checking: We check the conditions
# 𝑎 < 𝑏, 𝑐 > 𝑑 and 𝑎 × 𝑏 + 𝑐 × 𝑑 = 𝑀
# a×b+c×d=M. If a combination meets these conditions, it is printed directly.
# Password Tracking: We use a counter to track the number of valid combinations and store the fourth valid combination in the password variable.
# Output:
# If valid combinations are found, they are printed directly.
# If the fourth valid combination exists, it is printed as the password.
# If there are fewer than four valid combinations, "No!" is printed.