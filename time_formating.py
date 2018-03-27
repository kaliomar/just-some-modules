def readable(seconds):
    ''' this function takes time in seconds and return it in a human readable way '''
    minute = 60     # seconds
    hour = 3600     # seconds
    day = 86400     # seconds
    year = 31536000  # seconds
    time = []  # time =[years_count, years_format,
    ###        days_count, days_format,
    # hours_count,hours_format,
    ###        minutes_count, minutess_format,
    # seconds_count, seconds_format,]
    if seconds < 0:  # against negative numbers
        stru = "Error"
    if seconds == 0:  # against zero
        stru = "now"
    if seconds > 0:
        years = seconds // year
        time.append(years)
        # format
        if years == 1:
            form_y = "year"
            time.append(form_y)
        if years > 1:
            form_y = "years"
            time.append(form_y)
        if years == 0:
            form_y = "0"
            time.append(form_y)
        timeoveryears = seconds - (year * years)
        days = timeoveryears // day
        time.append(days)
        if days == 1:
            form_d = "day"
            time.append(form_d)
        if days > 1:
            form_d = "days"
            time.append(form_d)
        if days == 0:
            form_d = "0"
            time.append(form_d)
        timeoverdays = timeoveryears - (day * days)
        hours = timeoverdays // hour
        time.append(hours)
        if hours == 1:
            form_h = "hour"
            time.append(form_h)
        if hours > 1:
            form_h = "hours"
            time.append(form_h)
        if hours == 0:
            form_h = "0"
            time.append(form_h)
        timeoverhours = timeoverdays - (hour * hours)
        minutes = timeoverhours // minute
        time.append(minutes)
        if minutes == 1:
            form_m = "minute"
            time.append(form_m)
        if minutes > 1:
            form_m = "minutes"
            time.append(form_m)
        if minutes == 0:
            form_m = "0"
            time.append(form_m)
        timeoverminutes = timeoverhours - (minute * minutes)
        seconds = timeoverminutes
        time.append(seconds)
        if seconds == 1:
            form_s = "second"
            time.append(form_s)
        if seconds > 1:
            form_s = "seconds"
            time.append(form_s)
        if seconds == 0:
            form_s = "0"
            time.append(form_s)
        printout = []  # list to neglect parts which value == 0
        for i in range(0, len(time), 2):
            if time[i] > 0:
                printout.append(time[i])
                printout.append(time[i + 1])
        collective = []  # list to join every part with it's format e.g. [10, "years"] >>> '10 years'
        for i in range(0, (len(printout)), 2):
            member = str(printout[i]) + " " + printout[i + 1]
            collective.append(member)
            # next part just here for change the seperation of the last part of time from ", " to " and "
            # for example:
            # 10 days, 2 hours , 5 minutes >>>> 10 days, 2 hours and 5 minutes
            # stru is a function to convert list to string
            # for example:
            # ['10 days', '2 hours', '41 minutes', '1 second'] >>> 10 days, 2 hours, 41 minutes and 1 second
        for i in range(0, (len(collective) + 1)):
            if collective[-1] != collective[0]:
                stru = ', '.join(map(str, collective[0:-1])) + " " + "and" + " " + str(printout[-2]) + " " + printout[-1]
            else:
                stru = ' ,'.join(map(str, collective[:]))
    return stru


print readable(873661)
