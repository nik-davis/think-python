start_time = '6:52 am'
start_time_hour = 6
start_time_minute = 52
start_time_second = 0

start_time_total = (start_time_hour * 3600) + (start_time_minute * 60) + start_time_second

easy_pace = '8:15 per mile'
easy_pace_minutes = 8
easy_pace_seconds = 15
easy_pace_total = (easy_pace_minutes * 60) + easy_pace_seconds

fast_pace = '7:12 per mile'
fast_pace_minutes = 7
fast_pace_seconds = 12
fast_pace_total = (fast_pace_minutes * 60) + fast_pace_seconds

run_time = (easy_pace_total * 2) + (fast_pace_total * 3)

finish_time_total = start_time_total + run_time
finish_time_hour = finish_time_total // 3600
finish_time_minute = (finish_time_total % 3600) // 60
finish_time_second = (finish_time_total % 3600) % 60

finish_time = 'Finish time: {0}:{1} am'.format(finish_time_hour, finish_time_minute)
print(finish_time)
