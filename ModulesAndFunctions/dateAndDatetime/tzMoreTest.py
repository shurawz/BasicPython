import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time is {}.".format(local_time))
print("Naive utc time is {}.".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
# If above line of code is executed, it leads to print UTC on line 19
# If above line of code is followed by .astimezone() and executed, it leads to print place name from where it is executing
# on line 19
# astimezone() means according to the current timezone from where the code is executing


aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time: {} and time zone: {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time: {} and time zone: {}".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2018, 9, 26, 5, 56, 34)
print(gap_time)
print(gap_time.timestamp())
# Line-25....... It prints total number of seconds from 1st Jan 1970 to the given gap_time.

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(dt1)
print(dt2)

