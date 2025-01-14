time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

# Solution 1:
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")

# Solution 2: Ternanry operator -> not very optimal
# time = f"{minutes}:0{seconds}" if seconds < 10 else f"{minutes}:{seconds}"
# print(time)

#Solution3: most appropriate here, but w/o IF:
print(f"{minutes}:{seconds:02d}")