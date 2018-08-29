import time

def get_time_old():  
    raw_time = time.time()
    # print('Raw time: ', raw_time)

    years = raw_time // 31536000
    remainder = raw_time - (years * 31536000)
    # print('Years: ', years)

    days = remainder // 86400
    remainder -= (days * 86400)
    # print('Days: ', days)

    hours = remainder // 3600
    remainder -= (hours * 3600)
    # print('Hours: ', hours)

    minutes = remainder // 60
    remainder -= (minutes * 60)
    # print('Minutes: ', minutes)

    seconds = raw_time % 60
    # print('Seconds: ', seconds)
    seconds_alt = remainder
    # print('Seconds alt: ', seconds_alt)

    # epoch = 1 January 1970

    year = int(1970 + years)
    # print('Year: ', year)

    print('Time is {0}:{1} and {2} seconds.'.format(int(hours), int(minutes), int(seconds)))
    print('It has been {0} years and {1} days since the last epoch.'.format(int(years), int(days)))
    print('The year is currently {0}.'.format(int(year)))

get_time()