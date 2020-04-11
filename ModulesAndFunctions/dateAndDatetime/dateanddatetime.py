import time

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

#Like '%c' as first argument of strftime(), we have lots of such argument. Want to learn more ?
# go and visit "docs.python.org/3/library/time.html"

print("This current timezone is {0} with an offset of {1}.".format(time.tzname[0], time.timezone))

#time.timezone is negative in most of Western Europe, positive in the US, zero in the UK
#time.tzname gives the name of the timezone(so-called place) from where your are executing this code

print("Local time is " + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime()))

#If time.gmtime has 0 as parameter, it prints epoch time of the system.
#If time.gmtime has nothing as parameter, it prints UTC time .

# import datetime
# # import time
#
# print(datetime.datetime.today()) #current date and time
# print(datetime.datetime.now()) #current date and time
# print(datetime.datetime.utcnow()) #current date and time of UTC
