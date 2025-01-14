# read input for No of groups
groups = int(input())

# create counters:
count_musala = 0
count_mont_blanc = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

total_people = 0
for i in range(groups):
    group_size = int(input())
    total_people += group_size

    if 1 <= group_size <= 5:
        count_musala += group_size
    elif 6 <= group_size <= 12:
        count_mont_blanc += group_size
    elif 13 <= group_size <= 25:
        count_kilimanjaro += group_size
    elif 26 <= group_size <= 40:
        count_k2 += group_size
    elif group_size >= 41:
        count_everest += group_size

percentage_musala = (count_musala / total_people) * 100
percentage_mont_blanc = (count_mont_blanc / total_people) * 100
percentage_kilimanjaro = (count_kilimanjaro / total_people) * 100
percentage_k2 = (count_k2 / total_people) * 100
percentage_everest = (count_everest / total_people) * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_mont_blanc:.2f}%')
print(f'{percentage_kilimanjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')


