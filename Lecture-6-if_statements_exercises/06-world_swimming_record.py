RESISTANCE_SECONDS = 12.5
RESISTANCE_METERS = 15
record_in_seconds = float(input())
distance_in_meters= float(input())
seconds_per_meter= float(input())

water_resistance_time = distance_in_meters // RESISTANCE_METERS * RESISTANCE_SECONDS
swimmer_seconds = distance_in_meters * seconds_per_meter + water_resistance_time

if swimmer_seconds < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {swimmer_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {swimmer_seconds - record_in_seconds:.2f} seconds slower.")



