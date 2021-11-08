'time between dates'
def date():
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)
    print(now.weekday())
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print(days[now.weekday()])
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print(now.strftime('%A, %B, %d, %Y'))




