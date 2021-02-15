import calendar
import time
import datetime

# print(calendar.month(2020, 11, w=7, l=0))
# print(calendar.month(2020, 11, w=0, l=0))
# print(calendar.calendar(2020, w=2, l=0,c=2,m=3))
# print(calendar.weekday(2021, 2, 14))
# print(calendar.weekday(2021, 2, 15))
# print(calendar.leapdays(2000,2020))
# start = time.time()
# time.sleep(7)
# # print(time.time()) # from 01.01.1970 00:00
# # print(time.asctime())
# # print(time.gmtime())
# # print(type(time.gmtime()))
# # now = time.gmtime()
# # print(now[0],now[1],now[2])
# # print(now[0]+now[0])
#
# end = time.time()
# print(end-start)
#
#
# d = datetime.date(2018,7,22)
# print(d)
# print(type(d))
#
today = datetime.date.today()
# print(today)
#
# print(today-d)
#
# print(type(today.year))
# print(today.day)
#
# print(today.weekday())
# print(today.isoweekday())

# t = datetime.datetime.today()
# print(t)

#
# bday = datetime.datetime(2021,3,16)
# till_day = bday - today
# print(till_day)
# print(till_day.days)
# print(till_day.total_seconds())
#
# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# print(dt_today)
# print(dt_now)
# print(dt_today.strftime('%A,%d'))

dt_str = 'Nov 30, 2020'
str_to_date = datetime.datetime.strptime(dt_str,'%b %d, %Y')
print(str_to_date)

