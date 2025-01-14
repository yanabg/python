day_part = int(input())
week_day = input().lower()

working_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
weekend = ["sunday"]

if week_day in working_days and 10 <= day_part <= 18:
    print("open")
else:
    print("closed")
