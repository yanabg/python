from math import ceil

SUGAR_PACK = 950
FLOUR_PACK = 750

num_trumpets = int(input())

total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for _ in range(num_trumpets):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_pack_needed = ceil(total_sugar / SUGAR_PACK)
flour_pack_needed = ceil((total_flour / FLOUR_PACK))

print(f'Sugar: {sugar_pack_needed}')
print(f'Flour: {flour_pack_needed}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
