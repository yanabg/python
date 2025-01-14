total_student, total_standard, total_kid = 0, 0, 0

while True:
    movie_title = input()

    if movie_title == "Finish":
        break
    free_seats = int(input())
    sold_tickets = 0

    while sold_tickets < free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "student":
            total_student += 1
        elif ticket_type == "standard":
            total_standard += 1
        elif ticket_type == "kid":
            total_kid += 1

        sold_tickets += 1

    print(f'{movie_title} - {sold_tickets / free_seats * 100:.2f}% full.')

total_tickets = total_standard + total_student + total_kid
print(f'Total tickets: {total_tickets}')
print(f'{total_student / total_tickets * 100:.2f}% student tickets.')
print(f'{total_standard / total_tickets *100:.2f}% standard tickets.')
print(f'{total_kid / total_tickets * 100:.2f}% kids tickets.')
