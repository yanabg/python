CUP_PIC_PRICE = 40

stage = input()
ticket_type = input()
tickets_count = int(input())
pic_with_cup = input()

ticket_price = 0

if ticket_type == "Standard":
    if stage == "Quarter final":
        ticket_price = 55.50
    elif stage == "Semi final":
        performance = 75.88
    elif stage == "Final":
        ticket_price = 110.10
elif ticket_type == "Premium":
    if stage == "Quarter final":
        ticket_price = 105.20
    elif stage == "Semi final":
        ticket_price = 125.22
    elif stage == "Final":
        ticket_price = 160.66
elif ticket_type == "VIP":
    if stage == "Quarter final":
        ticket_price = 118.90
    elif stage == "Semi final":
        ticket_price = 300.40
    elif stage == "Final":
        ticket_price = 400

total_price = tickets_count * ticket_price

if total_price > 4000:
    total_price *= 0.75
    pic_with_cup = "N"
elif total_price > 2500:
    total_price *= 0.90
if pic_with_cup == "Y":
    total_price += tickets_count * 40

print(f'{total_price:.2f}')
