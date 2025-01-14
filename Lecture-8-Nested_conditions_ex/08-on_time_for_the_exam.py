exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute # 10 h * 60 min + 30 min
student_time_in_minutes = arrival_hour * 60 + arrival_minute #10 * 60 + 0

time_diff = exam_time_in_minutes - student_time_in_minutes # 630 - 600

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = abs(time_diff) // 60 # 90 / 60 = 1.5 => 1 time
minutes = abs(time_diff) % 60 # 90 % 60 => 30

result = ""

if hours > 0:
    result = f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result = f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0: # we dint use else because it will consider also =0  as after the start
    result += " after the start"

print(result)


