import sys

max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for i in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (sum_numbers - max_num))
    print("No")
    print(f'Diff = {diff}')