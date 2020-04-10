import time
from time import process_time

print(time.asctime())  #Prints the current time with date #At the moment, it prints 'Fri Apr 10 19:00:35 2020'

print(process_time())
    #Return the value (in fractional sec.s ) of the sum of the system and user CPU time of the current process.


t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

