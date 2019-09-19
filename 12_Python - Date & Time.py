import datetime
cur_date = datetime.datetime.now()

print(cur_date)
print('\n')
print(cur_date.year)
print('\n')
print(cur_date.day)
print('\n')
print(cur_date.weekday())
print('\n')
print(cur_date.month)
print('\n')
print(cur_date.time())
print('\n')

time1 = datetime.datetime.now()

time2 = datetime.timedelta(days=3)

time3 = time1+time2

print(time3.date())

print('\n')

####################### Date & Time Formats ########################
#Format Date and time
#The strftime() method takes a format specification and it formats the date or time based on that format.

#And the following table specifies some of the format options that you can use:

#%a          Prints locale abbreviated name of the weekday.

#%A         Prints the weekday.

#%w         Prints the day of the week as a number.

#%d          Prints the day of the month as a zero-padded number.

#%b          Prints the month as locale abbreviated name.

#%B          Prints the month as locale full name.

#%m        Prints the month as a zero-padded number.

#%y          Prints the year as a zero-padded two-digit number.

#%Y         Prints the year as a zero-padded four-digit number.

#%H         Prints the hour (24-hour clock) as a zero-padded number.

#%I           Prints the hour (12-hour clock) as a zero-padded number.

#%p          Prints AM or PM.

#%M        Prints the minute as a zero-padded number.

#%S          Prints the second as a zero-padded number.

date1 = datetime.datetime.now()
print(date1.strftime('%d %B %Y %I:%M%p'))

print('\n')

date2 = datetime.datetime.strptime('2019-09-19', '%Y-%m-%d')
print(date2)

print('\n')

date3 = datetime.datetime(year=2019, month=9, day=19)
print(date3)