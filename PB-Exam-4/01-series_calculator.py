serial_name = input()
seasons_num = int(input())
episodes_num = int(input())
regular_episode_duration = float(input())

adds_duration_for_one_episode = regular_episode_duration * 0.20
episodes_duration_with_adds = regular_episode_duration + adds_duration_for_one_episode
special_episodes_extra_time = seasons_num* 10
total_duration = episodes_duration_with_adds *\
                    episodes_num * seasons_num +\
                    special_episodes_extra_time

# print(f'ads_durstio {adds_duration_for_one_episode}')
# print(episodes_duration_with_adds)
# print(special_episodes_extra_time)
print(f'Total time needed to watch the {serial_name} series is {round(total_duration)} minutes.')