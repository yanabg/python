last_sector = input()
rows_in_first_sector = int(input())
seats_in_odd_row = int(input())

# initialize all seats counter
total_seats = 0

# loop over sectors from A to the last_sector=input()
for sector in range(ord('A'), ord(last_sector) + 1):
    current_sector = chr(sector)

    # calc. rows num for the current sector
    rows_in_current_sector = rows_in_first_sector + sector - ord('A')

    # loop over the current_sector_rows
    for row in range(1, rows_in_current_sector + 1):
        # define seats num in current row:
        if row % 2 != 0:
            seats_in_current_row = seats_in_odd_row
        else:
            seats_in_current_row = seats_in_odd_row + 2

        # loop over the seats in the current row
        for seat in range(1, seats_in_current_row + 1):
            current_seat = chr(ord('a') + seat - 1)
            print(f'{current_sector}{row}{current_seat}')
            total_seats += 1

# print total seats count:
print(total_seats)