import datetime
import pytz

#Working is simple but I must see all the functions and their functions to go further.

all_timezones = {'1': 'Asia/Kathmandu',
                 '2':  'Australia/Sydney',
                 '3':  'Australia/Melbourne',
                 '4': 'Zulu',
                 '5': 'Asia/Doha',
                 '6': 'Asia/Beijing',
                 '7': 'Australia/',
                 '8': 'Europe/Moscow',
                 '9': 'Europe/Moscow'
                }

for place in sorted(all_timezones):
    print("\t\t {}: {}".format(place, all_timezones[place]))


while True:
    num = input("Please enter any number from 1 to 9")


    if num == '0':
        exit()

    if num in all_timezones.keys():
        tz_to_display = pytz.timezone(all_timezones[num])
        local_time = datetime.datetime.now(tz=tz_to_display)
        print("Time of {} is {} {}.".format(all_timezones[place], local_time.strftime('%A %x %X %z'), local_time.tzname()))
        print("Local time is: ", datetime.datetime.now().strftime('%A %x %X'))
        print("UTC time is: ", datetime.datetime.utcnow().strftime('%A %x %X'))
        print()