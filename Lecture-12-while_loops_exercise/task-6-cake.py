width = int(input())
length = int(input())

total_pieces = width * length
# replacing lines 1,2 and 4 with this code only:
# total_pieces = int(input()) * int(input())
pieces_taken = 0

while True:
    cake_pieces_taken = input()

    if cake_pieces_taken == "STOP":
        break

    pieces_taken += int(cake_pieces_taken)

    if pieces_taken > total_pieces:
        break

if pieces_taken <= total_pieces:
    pieces_left = total_pieces - pieces_taken
    print(f'{pieces_left} pieces are left.')

else:
    pieces_needed = pieces_taken- total_pieces
    print(f'No more cake left! You need {pieces_needed} pieces more.')



