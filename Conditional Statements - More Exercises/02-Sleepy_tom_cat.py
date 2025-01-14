PLAY_NORM = 30000
PLAY_WORKING_DAY = 63
PLAY_NONWORKING_DAY = 127
DAYS_PER_YEAR = 365

non_working_days = int(input())

working_days = DAYS_PER_YEAR - non_working_days
real_play_time = (working_days * PLAY_WORKING_DAY) + (non_working_days * PLAY_NONWORKING_DAY)
deviation_from_norm = PLAY_NORM - real_play_time

# print(f"working days: {working_days}")
# print(f"real play time: {real_play_time}")
# print(f"norm deviation: {deviation_from_norm}")

abs_deviation_minutes = abs(deviation_from_norm)
hours = abs_deviation_minutes // 60
minutes = abs_deviation_minutes % 60

if real_play_time > PLAY_NORM:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
# print(f"{new_hours}:{new_minutes:02d}")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

