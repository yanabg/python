a1 = int(input())
a2 = int(input())
n = int(input())

# iterate over ASCII values for symbol 1 from a1 to a2 - 1
for s1 in range(a1, a2):
    if s1 % 2 == 1: # check if odd
        # iterate over range for symbol 2 from 1 to n-1
        for s2 in range(1, n):
            # iteration for symbol 3 from 1 to n / 2 - 1
            for s3 in range(1, n // 2):
                s4 = s1 # Symbol 4 is the ASCII value for s1
                if (s2 + s3 + s4) %2 == 1: # check if sum is odd
                    # print the ticket No in the required format:
                    print(f'{chr(s1)}-{s2}{s3}{s4}')


