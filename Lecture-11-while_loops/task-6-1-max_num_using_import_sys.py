import sys
from sys import maxsize

# Initialize largest to the smallest possible value
max_num = -sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break

    num = int(number)
    if num > max_num:
        max_num = num

print(max_num)
