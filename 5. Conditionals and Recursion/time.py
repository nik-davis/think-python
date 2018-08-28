import time

def get_time():
    '''Fetches current time since last epoch and returns current time
    of day, as well as number of days since last epoch
    '''
    raw_time = time.time() # 1535028652.8977334

    days = int(raw_time // 60 // 60 // 24)
    years = int(days // 365)
    remaining = raw_time - (days*60*60*24)

    hours = int(remaining // 60 // 60)
    remaining -= (hours*60*60)

    minutes = int(remaining // 60)
    seconds = int(raw_time % 60)

    if seconds < 10:
        seconds = '0{0}'.format(seconds)

    if minutes < 10:
        minutes = '0{0}'.format(minutes)

    print('Current time is: {0}:{1}:{2}'.format(hours, minutes, seconds))
    print('It has been {0} days ({1} years) since the last epoch'.format(days, years))

get_time()