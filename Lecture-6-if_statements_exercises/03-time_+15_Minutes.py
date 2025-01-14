# Solution 1:
#
# bonus_minutes = 15
#
# hours = int(input()) # 23
# minutes = int(input()) # 59
#
# minutes += bonus_minutes # 74
#
# if minutes > 59:
#     hours += 1 # 23 -> 24
#     minutes -= 60 # 74 - 60 -> 14
#
# if hours > 23:
#     hours -= 24 # 24 - 24 => 0
#
# print(f"{hours}:{minutes:02d}")

# Solution 2:
bonus_minutes = 15

hours = int(input()) # 23
minutes = int(input()) # 59

minutes += bonus_minutes # 74

total_minutes = hours * 60 + minutes + bonus_minutes

new_hours = total_minutes // 60 % 24 # 60 % 24 -> 24 % 24 => 0
new_minutes = total_minutes % 60



print(f"{new_hours}:{new_minutes:02d}")