import sys
from sys import maxsize

min_number = sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break

    num = int(number)
    if num <= min_number:
        min_number = num

print(min_number)

