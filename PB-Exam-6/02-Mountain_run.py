import math
from  math import  floor

record_seconds = float(input())
distance_meter = float(input())
time_seconds = float(input())

climbing_time = distance_meter * time_seconds

num_of_delays = math.floor(distance_meter / 50)
slope_delay = num_of_delays * 30

total_time = climbing_time + slope_delay

if total_time < record_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record_seconds:.2f} seconds slower.')


