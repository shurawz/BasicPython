import pytz
import datetime

country = 'Asia/Kathmandu'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("Local Time of {} is {}.".format(country, local_time))


#
# i = 0
# j = 0
# for x in pytz.all_timezones:
#     print(x)
#     j = j + 1
# #It prints all the place_name from where timezone is observed.
#
#
# for x in sorted(pytz.country_names):
#     # print(x + ": " + pytz.country_names[x])
#     print(pytz.country_names[x])
#     i = i + 1
#
# print(j) #592 places of timezones
# print(i)

for x in sorted(pytz.country_names):
    print("{0} : {1}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        print(pytz.country_timezones[x])
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t {} : {}".format(zone, local_time))

    else:
        print("No timezone is defined.")
