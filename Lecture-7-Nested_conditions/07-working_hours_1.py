current_hour = int(input())
week_day = input().lower()

if week_day == "monday" or week_day == "tuesday" or week_day == "wednesday" or week_day == "thursday"\
        or week_day == "friday" or week_day == "saturday":
    if 10 <= current_hour <= 18:
        print("opened")
    else:
        print("closed")
else:
    print("closed")