class Time:

    def __init__(self, h, min, s):
        if (h >= 0 and h < 23) and (min >= 0 and min < 60) and (s >= 0 and s < 60):
            Time.hour = h
            Time.minute = min
            Time.second = s
        else:
            print 'Invalid time'
