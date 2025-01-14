day_of_week = input().lower()
working_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekend = ["saturday", "sunday"]

if day_of_week in working_days:
    print("Working day")
elif day_of_week in weekend:
    print("Weekend")
else:
    print("Error")

