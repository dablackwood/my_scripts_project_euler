"""
You are given the following information, but you may prefer to do some
research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""

day = 2
tally = 0

months_common = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in xrange(1901, 2001):
    #print
    print year,
    if year % 4 == 0:
        months_current = months_leap
    else:
        months_current = months_common
    for month in xrange(0, 12):
        #print day, day % 7,
        if day % 7 == 0:
            tally = tally + 1
        day = day + months_current[month]
    print tally

print "*", tally
