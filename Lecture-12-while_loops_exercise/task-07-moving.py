width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
# total_space = int(input()) * int(input()) * int(input())
# repalces lines: 1,2,3 and 5
# print(f'total space is: {total_space}')

used_space = 0

while True:
    box_count = input()

    if box_count == "Done":
        break

    used_space += int(box_count)

    if used_space > total_space:
        break

if used_space <= total_space:
    free_space = total_space - used_space
    print(f'{free_space} Cubic meters left.')
else:
    missing_space = used_space - total_space
    print(f'No more free space! You need {missing_space} Cubic meters more.')
