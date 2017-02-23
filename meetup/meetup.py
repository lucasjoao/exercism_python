import sys
sys.path.insert(0, '/home/lucas/Workspace/python/exercism/python/leap')

from datetime import date
from leap import is_leap_year

day_as_int = {'Monday': 0,
              'Tuesday': 1,
              'Wednesday': 2,
              'Thursday': 3,
              'Friday': 4,
              'Saturday': 5,
              'Sunday': 6}

max_range_by_month = {1: 32,
                      2: 29,
                      3: 32,
                      4: 31,
                      5: 32,
                      6: 31,
                      7: 32,
                      8: 32,
                      9: 31,
                      10: 32,
                      11: 31,
                      12: 32}

def meetup_day(year, month, day, pos):
#     if pos == "teenth":
        # for i in range(13, 20):
            # if date(year, month, i).weekday() == day_as_int[day]:
                # return date(year, month, i)
#     elif pos
    applicants = []
    m = 30 if is_leap_year(year) else max_range_by_month[month]
    for i in range(1, m):
        if date(year, month, i).weekday() == day_as_int[day]:
            applicants.append(i)

    if pos == '1st':
        return date(year, month, applicants[0])
    elif pos == '2nd':
        return date(year, month, applicants[1])
    elif pos == '3rd':
        return date(year, month, applicants[2])
    elif pos == '4th':
        return date(year, month, applicants[3])
    elif pos == '5th':
        return date(year, month, applicants[4])
    elif pos == 'last':
        return date(year, month, applicants[-1])

    for j in applicants:
            if j in range(13, 20):
                return date(year, month, j)

