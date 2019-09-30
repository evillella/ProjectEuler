"""
Problem 19
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def update_day(d,n):
    return (d+n)%7

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
days = dict(zip(months,[31,28,31,30,31,30,31,31,30,31,30,31]))
day = 1 #sun = 0, mon = 1, tue = 2, wed = 3, thr = 4, fri = 5, sat = 6
#1900 not leap year because 1900 not divisible by 400
day = update_day(day, 31+28+31+30+31+30+31+31+30+31+30+31)
#this is the day of the week of 1 Jan 1901
year = 1901
sundays = 0
if day == 0:
    sundays+=1

while year<2001:
    for month in months:
        day = update_day(day,days[month])
        if day == 0:
            sundays+=1
    year += 1
    
print(sundays)
    

